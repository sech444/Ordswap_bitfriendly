import json
from itertools import groupby
import numpy as np
from bitcoinlib.db import *
from bitcoinlib.encoding import *
from bitcoinlib.keys import Address, BKeyError, HDKey, check_network_and_key, path_expand
from bitcoinlib.mnemonic import Mnemonic
from bitcoinlib.networks import Network
from bitcoinlib.values import Value, value_to_satoshi
from bitcoinlib.services.services import Service
from bitcoinutils.setup import setup
from bitcoinlib.mnemonic import Mnemonic
from hdwallet import HDWallet
from hdwallet.symbols import BTC
from bitcoinutils.setup import setup
from bitcoinutils.hdwallet import HDWallet
from bitcoinutils.keys import P2trAddress, PrivateKey
import binascii
import mnemonic
import bip32utils
#from blockcypher import get_address_overview
#import blockcypher
from fastapi.middleware.cors import CORSMiddleware

from hdwallet import HDWallet
from hdwallet.utils import generate_entropy
from hdwallet.symbols import BTC as SYMBOL
from typing import Optional
import requests
import json
import hashlib
import base58
import ecdsa
import bech32
import binascii
from bitcoinlib.wallets import Wallet
#from bitcoinlib.transactions import In
from fastapi import FastAPI, UploadFile, File, HTTPException, Depends, Form, Response, status
import shutil


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://bitfriendly.me",
    
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


def create_p2pkh_script_pubkey(public_key_hash):
    # Construct the P2PKH scriptPubKey
    script_pubkey = bytes.fromhex(f"76a914{public_key_hash}88ac")
    return script_pubkey





@app.get("/HDwallets")
def generate_btc_private_key():
    # Choose strength 128, 160, 192, 224 or 256
    STRENGTH: int = 128  # Default is 128
    # Choose language english, french, italian, spanish, chinese_simplified, chinese_traditional, japanese or korean
    LANGUAGE: str = "english"  # Default is english
    # Generate new entropy hex string
    ENTROPY: str = generate_entropy(strength=STRENGTH)
    # Secret passphrase for mnemonic
    PASSPHRASE: Optional[str] = None  # "meherett"
    print(PASSPHRASE)
    # Initialize Bitcoin mainnet HDWallet
    hdwallet: HDWallet = HDWallet(symbol=SYMBOL, use_default_path=False)
    # Get Bitcoin HDWallet from entropy
    hdwallet.from_entropy(
        entropy=ENTROPY, language=LANGUAGE, passphrase=PASSPHRASE
    )

    hdwallet.from_path("m/44'/0'/0'/0/1")
    # Print all Bitcoin HDWallet information's
    print(json.dumps(hdwallet.dumps(), indent=4, ensure_ascii=False))
    wallet_id = json.dumps(hdwallet.dumps(), indent=4, ensure_ascii=False)
    wallet_info =  json.loads(wallet_id)

    public_key = wallet_info['public_key']
    # Example usage
    public_key_hash = public_key
    p2pkh_script = create_p2pkh_script_pubkey(public_key_hash)
    print(f"P2PKH ScriptPubKey: {p2pkh_script.hex()}")

    
    taproot_address = p2pkh_script #wallet_info['addresses']['p2sh'],
    #taproot = ['taproot_address']
    print(taproot_address)
    taproot = taproot_address # Extract the address from the list
    
   
    
    
    encoded_taproot = encode_taproot_address(taproot_address)
    print("Bech32 encoded taproot address:", encoded_taproot)




    
    return{
        'public_key': wallet_info['public_key'],
        'mnemonic' :  wallet_info['mnemonic'],
        'taproot_address':  encoded_taproot,
        'private_key':  wallet_info['private_key'],
        "addresses" : wallet_info['addresses'],
    }
  

from bitcoin_value import currency

# Specify the currency code (e.g., "USD", "EUR")
bitcoin_value = currency("USD")

# Print the Bitcoin value in the specified currency
print(f"1 BTC is equivalent to {bitcoin_value} USD")



def encode_taproot_address(taproot_address):
    try:
        # Convert taproot address to bytes
        spk = binascii.unhexlify(taproot_address)
        version = spk[0] - 0x50 if spk[0] else 0
        encoded_address = bech32.encode('bc', version, spk[2:])
        return encoded_address
    except binascii.Error:
        return "Invalid hexadecimal format in taproot address."


@app.get("/recover_wallet")
def recover_wallet(mnemonic_words: str):
    # Create a BIP44HDWallet instance
    hdwallet = HDWallet(symbol=BTC)

    # Get wallet from mnemonic
    hdwallet.from_mnemonic(mnemonic=mnemonic_words)

    # Derive for the path
    hdwallet.from_path("m/44'/0'/0'/0/1")

    # Print all Bitcoin HDWallet information's
    print(json.dumps(hdwallet.dumps(), indent=4, ensure_ascii=False))

    wallet_info =  json.loads(json.dumps(hdwallet.dumps(), indent=4, ensure_ascii=False))

    pub = wallet_info['public_key']
     # Step 1: Hash the public key
    public_key = bytes.fromhex(pub)
    hash_pubkey = hashlib.sha256(public_key).digest()

    # Step 2: Derive the Taproot address
    address_bytes = bytes.fromhex("bc") + hash_pubkey

    # Step 3: Convert the bytes to base58 format
    taproot_address = base58.b58encode_check(address_bytes).decode('utf-8')

    return{
        "Taproot Address" : taproot_address,
        'public_key': wallet_info['public_key'],
        'mnemonic' :  wallet_info['mnemonic'],
        'addresses':  wallet_info['addresses'],
        'private_key':  wallet_info['private_key']
    }


@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    with open(file.filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename}



@app.post("/api/v1/bitcoin_transaction", tags=["Transaction"])
def bitcoin_transaction(Private_key: str = Form(...),  addr_to: str = Form(...), value: str = Form(...), ):

    try:
        addr_to = addr_to
        value = value
        my_key = Key(priv_key)
        outputs = [(addr_to, value, 'btc')]
        data = my_key.send(outputs)
        return{"data": data}
    except ValueError as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                       detail=f"InsufficientFunds plus estimated_fee")

#from blockcypher import get_address_overview
@app.post("/api/v1/get_btc_bals", tags=["Transaction"])
def btc_bals(
    #response: Response,
   # token: str = Depends(token_auth_scheme),
    user_addr: str = Form(...),
):
    """A valid access token is required to access this route"""

    # result = VerifyToken(token.credentials).verify()  # 👈 updated code

    # # 👇 new code
    # if result.get("status"):
    #     response.status_code = status.HTTP_400_BAD_REQUEST
    #     return result


    try:
        balance_data = blockcypher.get_address_details(user_addr)
        #print(balance_data)
        
        final_balance = balance_data['final_balance']

        #print(final_balance)
        bals = blockcypher.from_base_unit(final_balance, 'btc')
        return {"BTC": bals}
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Not a valid btc address"
        )








# docker run -p 8080:84 -d sech44/bitfriendly-api:0.0.3


def encode_taproot_address():
    try:
        # Convert taproot address to bytes
        spk = binascii.unhexlify('0014751e76e8199196d454941c45d1b3a323f1433bd6')
        version = spk[0] - 0x50 if spk[0] else 0
        program = spk[2:]
        print(bech32.encode('bc', version, program))
        encoded_address = bech32.encode('bc', version, program)
        return encoded_address
    except binascii.Error as e:
        print(e)
        return "Invalid hexadecimal format in taproot address."


encode_taproot_address()

import base58check

def base58_to_hex(base58_address):
    decoded_data = base58check.b58decode(base58_address)
    hex_representation = decoded_data.hex()
    return hex_representation

taproot_address_base58 = '35pxzrPBHAs3ME6PTcUCJCk4W6qi4sp5eQ'
hex_representation = base58_to_hex(taproot_address_base58)
print(hex_representation)

def create_p2pkh_script_pubkey(public_key_hash):
    # Construct the P2PKH scriptPubKey
    script_pubkey = bytes.fromhex(f"76a914{public_key_hash}88ac")
    return script_pubkey

# Example usage
public_key_hash = "02406dbbc4e805229be5a085a1fc0a6276c02cbb"
p2pkh_script = create_p2pkh_script_pubkey(public_key_hash)
print(f"P2PKH ScriptPubKey: {p2pkh_script.hex()}")

import hashlib

# public_key = '034dcbcf4ca2aa27b9ee9b07095d69901f134cdbb1ea93383b648685ff1fd938e7'

# Convert the public key to bytes
public_key_bytes = bytes.fromhex(public_key)

# Hash the public key using SHA-256
sha256_hash = hashlib.sha256(public_key_bytes).digest()

# Hash the result again using RIPEMD-160
ripemd160_hash = hashlib.new('ripemd160', sha256_hash).hexdigest()

print(f"The public key hash of {public_key} is {ripemd160_hash}")

public_key=public_key

import hashlib
from bitcoinlib.keys import Address

public_key = "public_key"  # input("Enter public key: ")

# Take SHA256 hash of public key
sha256 = hashlib.sha256(bytes.fromhex(public_key)).digest()

# Take RIPEMD160 hash of SHA256 hash
ripemd160 = hashlib.new('ripemd160', sha256).digest()

# Add network byte
network_byte = b'\x00'  # Mainnet
extended_ripemd160 = network_byte + ripemd160

# Ensure the length of the extended RIPEMD160 is 21 bytes (1 byte network + 20 bytes RIPEMD160)
if len(extended_ripemd160) != 21:
    raise ValueError("Incorrect length of extended RIPEMD160")

# Create address object without specifying the network parameter
address = Address(hashed_data=ripemd160, encoding='bech32')

# Print bech32 address
print(address.address)

return password has be taken "@app.post("/users/", response_model=schemas.UserResponse)
def create_user(password_input: schemas.PasswordInput, db: Session = Depends(get_db)):
    # Check password strength
    if password_input.password == security.check_password_strength(password_input.password):
        raise HTTPException(status_code=400, detail=utils.check_password_strength(password_input.password))

    # Confirm passwords match
    if password_input.password != password_input.confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")

    # Generate mnemonic
    wallet_info = generate_btc_private_key()

    # This is your provided public key
    public_key =  wallet_info['public_key']

    # Perform SHA-256 hashing on the public key
    sha256 = hashlib.sha256(binascii.unhexlify(public_key)).digest()

    # Perform RIPEMD-160 hashing on the SHA-256 hash
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(sha256)
    hash160 = ripemd160.digest()

    # Convert the hash160 to an array of 5-bit unsigned integers
    five_bit_pub_key = convertbits(hash160, 8, 5)

    # Witness version
    witver = 1

    # Encode the address
    address = bech32_encode('bc', [witver] + five_bit_pub_key)

    mnemonic_list = wallet_info['mnemonic']
    mnemonic = mnemonic_list.split(' ')

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


    # Create user
    user_data = schemas.UserCreate(password=password_input.password)
    db_user = crud.create_user(db=db, password=password_input.password, user=user_data, mnemonic=mnemonic_item)

    # Update owner_id for mnemonic_item
    db_mnemonic = crud.update_mnemonic_owner_id(db=db, mnemonic_id=db_user.id, owner_id=db_user.id)

    private_key = wallet_info['private_key']
    addresses = address 

    return {'mnemonic': mnemonic,
            'private_key': private_key,
            "addresses": addresses
            }




# import subprocess

# mnemonic = "olympic wine chicken argue unaware bundle tunnel grid spider slot spell need"
# derivation = "bip86"

# # Build the command
# command = ["btc_address_dump", "-d", derivation, mnemonic]

# # Run the command
# result = subprocess.run(command, capture_output=True, text=True)

# # Print the result
# print(result.stdout)

# WOrking docker frontend

# FROM node:18.19.0-slim

# ENV PATH /app/node_modules/.bin:$PATH


# WORKDIR /app

# RUN npm install -g @vue/cli@5.0.8

# COPY app/package.json ./

# COPY app/package-lock.json ./

# RUN npm install

# COPY --chown=node:node . .

# USER node

# CMD ["npm", "run", "serve"]



# # (FROM python:3.10.13-alpine

# # Install system dependencies
# RUN apk update && apk add --no-cache sqlite sqlite-dev build-base gmp-dev gcc

# # Use built-in pip to access poetry
# RUN  pip install --upgrade pip

# RUN pip install --progress-bar off "poetry==1.7.0"




# RUN pip install ecdsa[gmpy2]
# RUN pip install blockcypher
# RUN pip install --upgrade setuptools
# RUN pip wheel --no-cache-dir --use-pep517 "h5py (==3.9.0)"

# # Set working directory
# WORKDIR /app



# # Copy only the necessary files
# COPY pyproject.toml poetry.lock* /app/

# # Project initialization
# RUN poetry config virtualenvs.create false && poetry install --no-interaction

# # Allow installing dev dependencies to run tests
# ARG INSTALL_DEV=false
# RUN if [ "$INSTALL_DEV" = "true" ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi

# # For development, Jupyter remote kernel, Hydrogen
# ARG INSTALL_JUPYTER=false
# RUN if [ "$INSTALL_JUPYTER" = "true" ] ; then pip install jupyterlab ; fi

# # Copy the rest of the application
# COPY . /app

# # Expose the necessary port
# #EXPOSE 84/tcp

# # Command to run the application
# #CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "84"]
# )