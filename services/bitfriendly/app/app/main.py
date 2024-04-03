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
from endpoint import send_btc
from user import models, utils

import bech32
# from fastapi import FastAPI, UploadFile, File, HTTPException, Depends, Form, Response, status,Query
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

# users_router.py
# In your main.py file
from endpoint.send_btc import router as send_btc_router 

# from users_router import router as users_router

app = FastAPI()
#app.include_router(items_router) 
app.include_router(send_btc_router) 

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
    
    #passworw can't be none
    if password_input.password == None :
        raise HTTPException(status_code=400, detail="Passwords do not be empty")


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
            raise HTTPException(status_code=400, detail="Password not valid choose another password")

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
    #print(mnemonic)
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
    return {"message": "Welcome to Bitfriendly API"}







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

    #print(result)

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

# @app.post("/uploadfile/")
# async def upload_file(file: UploadFile = File(...)):
#     with open(file.filename, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     return {"filename": file.filename}



@app.post("/bitcoin_transaction", tags=["Transaction"])
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


@app.post("/ordinal_inscription", tags=["Transaction"])
async def ordinal_inscription(Private_key: str = Form(...), addr_to: str = Form(...)):
    # Assuming `user` is an instance of some class that contains the `sendbtc_ordinal_inscription` method
    snedBTC = user.sendbtc_ordinal_inscription(addr_to, Private_key)
    return {"data": snedBTC}

@app.get("/estimates_gas_free", tags=["Transaction"])
async def estimates_gas_free(request: Request):

    # URL of the Blockstream Esplora API fee estimates endpoint
    node_url = "https://blockstream.info/api/fee-estimates"

    response = requests.get(node_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        fee_estimates = response.json()

       
        # Define the confirmation targets for default fees
        targets = {"fast": 1, "normal": 25, "slow": 144}

        # Dictionary to store the formatted fee estimates
        result = {}

        # Loop through the targets to get the fee estimates
        for label, target in targets.items():
            fee_estimate = fee_estimates.get(str(target))
            if fee_estimate is not None:
                rounded_fee_estimate = round(fee_estimate, 2)  # Round to 2 decimal places
                result[label] = f" {rounded_fee_estimate} sat/vB"
            else:
                result[label] = f"{label.capitalize()} fee estimate not available"

        # Handle Custom Choose Fee (enhanced logic)
        custom_fee = request.query_params.get("custom_fee")  # Access custom fee from query string
        if custom_fee:
            try:
                custom_fee = int(custom_fee)  # Attempt conversion to integer
                if custom_fee >= 0:
                    rounded_custom_fee = round(custom_fee, 2)  # Round custom fee to 2 decimal places
                    result["custom"] = f" {rounded_custom_fee} sat/vB (rounded up to 2 decimals)"
                else:
                    result["custom_error"] = "Custom fee cannot be negative."
            except ValueError:
                result["custom_error"] = "Invalid custom fee value. Please enter a number."

        return result

    else:
        print("Error:", response.text)
        return {"error": "Failed to fetch fee estimates."}  # Handle unsuccessful response

# @app.get("/estimates_gas_free", tags=["Transaction"])
# async def estimates_gas_free():
   
#     # URL of the Blockstream Esplora API fee estimates endpoint
#     node_url = "https://blockstream.info/api/fee-estimates"

#     response = requests.get(node_url)

#     # Check if the request was successful
#     if response.status_code == 200:
#         # Parse the JSON response
#         fee_estimates = response.json()

#         # Define the confirmation targets for fast, normal, and slow fees
#         targets = {"fast": 1, "normal": 6, "slow": 24}

#         # Dictionary to store the formatted fee estimates
#         result = {}

#         # Loop through the targets to get the fee estimates
#         for label, target in targets.items():
#             fee_estimate = fee_estimates.get(str(target))
#             if fee_estimate is not None:
#                 result[label] = f" {fee_estimate} sat/vB"
#             else:
#                 result[label] = f"{label.capitalize()} fee estimate not available"

#         return result

#     else:
#         print("Error:", response.text)


@app.post("/get_balance", tags=["Transaction"])
async def get_balance(address: str = Form(...)):
    try:
        # URL of the Blockstream Esplora API address endpoint
        node_url = f"https://blockstream.info/api/address/{address}"

        # Send a GET request to fetch the address information
        response = requests.get(node_url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            result = response.json()
            return result
        else:
            # Raise an HTTPException with the appropriate status code and message
            raise HTTPException(status_code=response.status_code, detail=response.text)
    except json.decoder.JSONDecodeError as e:
        # Handle JSON decoding errors
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@app.post("/create_transaction", tags=["Transaction"])
async def create_transaction(address: str = Form(...), wallet_name: str = Form(...),
                              document_id: str = Form(...), timestamp: str = Form(...),
                              author: str = Form(...), content: str = Form(...)):
    try:
        # Fetch UTXOs for the address
        utxos_url = f"https://blockstream.info/api/address/{address}/utxo"
        response = requests.get(utxos_url)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        utxos = response.json()

        # Create a transaction
        tx = Transaction()

        # Add inputs (unspent outputs) to the transaction
        for utxo in utxos:
            tx.add_input(TxInput(txid=utxo['txid'], index=utxo['vout']))

        # Add metadata to embed into the blockchain
        metadata = {
            "document_id": document_id,
            "timestamp": timestamp,
            "author": author,
            "content": content
        }

        # Convert metadata to JSON and encode it
        metadata_json = json.dumps(metadata)
        metadata_encoded = metadata_json.encode("utf-8")

        # Add OP_RETURN output with the encoded metadata
        op_return_output = TxOutput(script='OP_RETURN ' + metadata_encoded.hex())

        # Add OP_RETURN output to the transaction
        tx.add_output(op_return_output)

         # Sign the transaction with the private keys of the inputs
        tx.sign(Wallet(wallet_name).keys)

        # Return the serialized transaction
        return {"serialized_transaction": tx.serialize()}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Example usage:
# GET http://localhost:8000/estimates_gas_free
# Response: {"fast": 34.498, "normal": 25.726, "slow": 24.409}


# mnemonic = "olympic wine chicken argue unaware bundle tunnel grid spider slot spell need"
# derivation = "bip84"

# # Build the command
# command = ["btc_address_dump", "-d", derivation, mnemonic]

# # Run the command
# result = subprocess.run(command, capture_output=True, text=True)

# # Print the result
# print(result.stdout)


@app.post("/broadcast_transaction", tags=["Transaction"])
async def broadcast_transaction(your_address: str = Form(...), your_password: str = Form(...)):
    try:
        # Create a wallet object
        wallet = Wallet("my_wallet")

        # Create a transaction
        tx = P2PKH.create_simple(
            inputs=[],
            outputs=[(0.0, your_address)],  # Send the remaining funds back to your address
            fee=0.0001  # Transaction fee in BTC
        )

        # Add OP_RETURN output with your data
        data = "Hello, Bitcoin!"
        op_return_script = P2PKH.compile('OP_RETURN ' + data.encode("utf-8").hex())

        # Add OP_RETURN output to the transaction
        tx.add_outputs([(0, op_return_script)])

        # Sign the transaction
        tx.sign(keys=wallet.keys, password=your_password)

        # Serialize the transaction
        serialized_tx = tx.serialize()

        # Broadcast the transaction using Blockstream's API
        broadcast_url = "https://blockstream.info/testnet/api/tx"
        response = requests.post(broadcast_url, data=serialized_tx)

        # Check if the broadcast was successful
        if response.status_code == 200:
            return {"message": "Transaction broadcasted successfully"}
        else:
            return {"error": "Failed to broadcast transaction"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))






