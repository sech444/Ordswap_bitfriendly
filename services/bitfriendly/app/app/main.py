import json
from itertools import groupby
import numpy as np

from bitcoinutils.setup import setup
from bitcoinutils.setup import setup
from bitcoinutils.hdwallet import HDWallet
from bitcoinutils.keys import P2trAddress, PrivateKey
import binascii
from mnemonic import Mnemonic
import bip32utils
from fastapi.middleware.cors import CORSMiddleware
from hdwallet import HDWallet
from hdwallet.utils import generate_entropy
from hdwallet.symbols import BTC as SYMBOL
from typing import Optional
import requests
import hashlib
import base58
import ecdsa
from user import models, utils
import bech32
from fastapi import FastAPI, UploadFile, File, HTTPException, Depends, Form, Response, status,Query
import shutil

from bech32m_chia import bech32m
from sqlalchemy.orm import Session
import jwt
from app.core import crud, schemas, security
from .db import *
from fastapi import (APIRouter, BackgroundTasks, Depends, FastAPI, Form,
                     HTTPException, Response, WebSocket, status)

from datetime import timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import bcrypt
import hashlib
import binascii
from bech32 import bech32_encode, convertbits
from fastapi.security import HTTPBearer
from fastapi import Depends, FastAPI, HTTPException, Request, Response
from sqlalchemy import or_
from fastapi.security import OAuth2PasswordBearer

token_auth_scheme = HTTPBearer()

from starlette.middleware.cors import CORSMiddleware
import subprocess

from app.core.config import settings
import os
app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)


# Set all CORS enabled origins
# if settings.BACKEND_CORS_ORIGINS:
#     app.add_middleware(
#         CORSMiddleware,
#         allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
#         allow_credentials=True,
#         allow_methods=["*"],
#         allow_headers=["*"],
#     )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#app.include_router(api_router, prefix=settings.API_V1_STR)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response






models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")




@app.post("/token", response_model=schemas.UserLoginResponse)
async def login_for_access_token(form_data: schemas.UserLogin, db: Session = Depends(get_db)):

    if form_data.password is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password is required",
        )

    user = crud.authenticate_user(db, password=form_data.password)
   
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(subject=str(user.id), expires_delta=access_token_expires)

    mnemonics: List[models.Item] = user.mnemonics
    
    # Create a list containing all mnemonic items from 0 to 11
    mnemonic_item = [
        [
            item.mnemonic_1,
            item.mnemonic_2,
            item.mnemonic_3,
            item.mnemonic_4,
            item.mnemonic_5,
            item.mnemonic_6,
            item.mnemonic_7,
            item.mnemonic_8,
            item.mnemonic_9,
            item.mnemonic_10,
            item.mnemonic_11,
            item.mnemonic_12,
        ]
        for item in mnemonics
    ]
    


    flat_mnemonic_list = [word for sublist in mnemonic_item for word in sublist]

    # Convert the list to a space-separated string
    mnemonic_string = ' '.join(flat_mnemonic_list)

    # Recover wallet from mnemonic string
    wallet_info = recover_wallet(mnemonic_string)
  

    # Access the Taproot Address and private_key
    taproot_address = wallet_info['bech32m_address_p2tr']
    private_key = wallet_info['private_key_WIF_compressed']

    
    crud.update_last_login(db, user.id)  # Update last login time

    return {"access_token": access_token,
                "token_type": "bearer",
                "mnemonic_item": mnemonic_item,
                "taproot_address": taproot_address,
                "private_key": private_key,

                }


@app.post("/users/", response_model=schemas.UserResponse)
def create_user(password_input: schemas.PasswordInput, mnemonic: Optional[str] = None, db: Session = Depends(get_db)):
    # Check password strength
    if password_input.password == security.check_password_strength(password_input.password):
        raise HTTPException(status_code=400, detail=utils.check_password_strength(password_input.password))

    # Confirm passwords match
    if password_input.password != password_input.confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")
    
    # Fetch all users with hashed passwords from the database
    users_with_passwords = db.query(models.User).filter(models.User.hashed_password.isnot(None)).all()

    # Check each user for a match with the entered password
    for user_with_password in users_with_passwords:
        if security.verify_password(password_input.password, user_with_password.hashed_password):
            raise HTTPException(status_code=400, detail="Password has already been taken")

    if mnemonic is None:
        # If mnemonic is not provided, generate a new one
        info = generate_btc_private_key()
        wallet_info = info
        mnemonic_list = wallet_info['mnemonic'].split()
    else:
        # Mnemonic is provided
        wallet_info = generate_btc_private_key(mnemonic)
        mnemonic_list = mnemonic.split()
    # Convert the list to a space-separated string to store in the database
    mnemonic = mnemonic_list
    print(mnemonic)
    # Create mnemonic item

    mnemonic_item = schemas.Item(
       
        mnemonic_1=mnemonic[0],
        mnemonic_2=mnemonic[1],
        mnemonic_3=mnemonic[2],
        mnemonic_4=mnemonic[3],
        mnemonic_5=mnemonic[4],
        mnemonic_6=mnemonic[5],
        mnemonic_7=mnemonic[6],
        mnemonic_8=mnemonic[7],
        mnemonic_9=mnemonic[8],
        mnemonic_10=mnemonic[9],
        mnemonic_11=mnemonic[10],
        mnemonic_12=mnemonic[11],
        owner_id=None  # Placeholder for owner_id, to be updated later
    )
    #if not crud.all_mnemonic_words_exist(db, mnemonic):

    # Create user
    user_data = schemas.UserCreate(password=password_input.password)
    db_user = crud.create_user(db=db, password=password_input.password, user=user_data, mnemonic=mnemonic_item)

    # Update owner_id for mnemonic_item
    db_mnemonic = crud.update_mnemonic_owner_id(db=db, mnemonic_id=db_user.id, owner_id=db_user.id)

  
    return {'mnemonic': mnemonic,
            'private_key': wallet_info['private_key_WIF_compressed'],
            "addresses": wallet_info['bech32m_address_p2tr']
            }




@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users




@app.get("/")
def read_root():
    return {"Hello": "World"}







from typing import _GenericAlias

@app.get("/HDwallets")
def generate_btc_private_key(mnemonic: Optional[str] = None):

    if mnemonic is None:
        # If mnemonic is not provided, generate a new one
        mnemonic = Mnemonic("english").generate(strength=128)
        #print(mnemonic)
    # Ensure mnemo is a string
    mnemonic = str(mnemonic)

    # Create a BIP44HDWallet instance
   
    is_valid = crud.is_valid_mnemonic(mnemonic)

    if is_valid:
        words = mnemonic

        # Derivation path
        derivation = "bip86"

        # Build the command
        command = ["btc_address_dump", "-d", derivation, words]

        # Run the command
        result = subprocess.run(command, capture_output=True, text=True)

        # Extract the wallet information from the command output
        wallet_info = {}
        for line in result.stdout.split("\n"):
            if "=" in line:
                key, value = line.split("=")
                wallet_info[key.strip()] = value.strip()
    else:
        #print("Mnemonic is not valid.")
        raise HTTPException(status_code=400, detail="Mnemonic is not valid")

    # Check if the keys exist in the dictionary before accessing them
    return {
        'mnemonic': words,
        'private_key_hex': wallet_info.get('private key (hex)', None),
        'private_key_WIF': wallet_info.get('private key (WIF)', None),
        'private_key_WIF_compressed': wallet_info.get('private key (WIF compressed)', None),
        'taproot_tweaked_private_key': wallet_info.get('taproot tweaked private key', None),
        'public_key_compressed': wallet_info.get('public key (compressed)', None),
        'hash160_of_compressed_public_key': wallet_info.get('hash160 of compressed public key', None),
        'taproot_tweaked_public_key': wallet_info.get('taproot tweaked public key (taproot output key)', None),
        'bech32m_address_p2tr': wallet_info.get('bech32m address (p2tr)', None),
    }




@app.get("/recover_wallet")
def recover_wallet(mnemonic_words: str):
    
    # Create a BIP44HDWallet instance
    is_valid = crud.is_valid_mnemonic(mnemonic_words)

    if is_valid:
        pass
    else:
        #print("Mnemonic is not valid.")
        raise HTTPException(status_code=400, detail="Mnemonic is not validh")


    # Get wallet from mnemonic
   # Derivation path
    derivation = "bip86"

    # Build the command
    command = ["btc_address_dump", "-d", derivation, mnemonic_words]

    # Run the command
    result = subprocess.run(command, capture_output=True, text=True)


    # Extract the wallet information from the command output
    wallet_info = {}
    for line in result.stdout.split("\n"):
        if "=" in line:
            key, value = line.split("=")
            wallet_info[key.strip()] = value.strip()

   # Check if the keys exist in the dictionary before accessing them
   
    return {
            'mnemonic': mnemonic_words,
            'private_key_hex': wallet_info.get('private key (hex)', None),
            'private_key_WIF': wallet_info.get('private key (WIF)', None),
            'private_key_WIF_compressed': wallet_info.get('private key (WIF compressed)', None),
            'taproot_tweaked_private_key': wallet_info.get('taproot tweaked private key', None),
            'public_key_compressed': wallet_info.get('public key (compressed)', None),
            'hash160_of_compressed_public_key': wallet_info.get('hash160 of compressed public key', None),
            'taproot_tweaked_public_key': wallet_info.get('taproot tweaked public key (taproot output key)', None),
            'bech32m_address_p2tr': wallet_info.get('bech32m address (p2tr)', None),
        }

@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    with open(file.filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename}



@app.post("/api/v1/bitcoin_transaction", tags=["Transaction"])
async def bitcoin_transaction(Private_key: str = Form(...),  addr_to: str = Form(...), value: str = Form(...), ):
    from bit import Key
   
    
    try:
        addr_to = addr_to
        print(addr_to)
        value = value
        my_key = Key(Private_key)
        print(my_key)
        my_wallet = my_key.address
        print(my_wallet)
        p2wsh = my_key.segwit_address
        print(p2wsh)
        balance_data = my_key.get_balance('usd')
        print(balance_data)
        outputs = [(addr_to, value, 'btc')]
        data = my_key.send(outputs)
        return{"data": data}
    except ValueError as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                       detail=f"json.dumps(SystemExit(e))")


# # from blockcypher import get_address_overview
# @app.post("/api/v1/get_btc_bals", tags=["Transaction"])
# def btc_bals(
#     #response: Response,
#    # token: str = Depends(token_auth_scheme),
#     user_addr: str = Form(...),
# ):
#     """A valid access token is required to access this route"""

#     # result = VerifyToken(token.credentials).verify()  # 👈 updated code

#     # # 👇 new code
#     # if result.get("status"):
#     #     response.status_code = status.HTTP_400_BAD_REQUEST
#     #     return result

#     try:
#         balance_data = blockcypher.get_address_details(user_addr)
#         #print(balance_data)
        
#         final_balance = balance_data['final_balance']

#         #print(final_balance)
#         bals = blockcypher.from_base_unit(final_balance, 'btc')
#         return {"BTC": bals}
#     except Exception as e:
#         print(e)
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail=f"Not a valid btc address"
#         )



# import subprocess

# mnemonic = "olympic wine chicken argue unaware bundle tunnel grid spider slot spell need"
# derivation = "bip84"

# # Build the command
# command = ["btc_address_dump", "-d", derivation, mnemonic]

# # Run the command
# result = subprocess.run(command, capture_output=True, text=True)

# # Print the result
# print(result.stdout)