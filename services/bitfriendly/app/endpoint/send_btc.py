from bitcoinlib.wallets import Wallet
from bitcoinlib import *
from fastapi import APIRouter
from fastapi import FastAPI, UploadFile, File, HTTPException, Depends, Form, Response, status,Query
router = APIRouter()

import hashlib
from buidl.ecc import PrivateKey
from buidl.helper import big_endian_to_int
from buidl.script import P2PKHScriptPubKey
from buidl.tx import Tx, TxIn, TxOut



router = APIRouter(
    prefix="/users",
    tags=["Transaction"]
)
#from bitcoinlib.networks import Network, networks 

def sendbtc_ordinal_inscription(your_address, your_password):
 
   

    # Connect to a Bitcoin node, e.g., a local Bitcoin Core instance
    Wallet.connect(node_alias="local")

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
    tx.sign(keys=wallet.keys, password="your_password")

    # Broadcast the transaction to the Bitcoin network
    tx.broadcast()

    # Disconnect from the Bitcoin node
    Wallet.disconnect()




from bitcoinutils.setup import setup
from bitcoinutils.utils import to_satoshis
from bitcoinutils.transactions import Transaction, TxInput, TxOutput, TxWitnessInput
from bitcoinutils.keys import P2pkhAddress, PrivateKey
from pycoin.symbols.btc import network
import asyncio

from fastapi import HTTPException
import requests

@router.post("/users/", tags=["Transaction"])
async def main_transaction(Private_key: str = Form(...),  addr_to: str = Form(...), amount: str = Form(...), gasfee: str = Form(...), ):
    try:
        # always remember to setup the network
        setup('mainnet')

        # the key that corresponds to the P2WPKH address
        priv = PrivateKey(Private_key)

        pub = priv.get_public_key()

        fromAddress = pub.get_taproot_address()
        print(fromAddress.to_string())

        # UTXO of fromAddress
        # Fetch UTXOs for the address
        utxos_url = f"https://blockstream.info/api/address/{address}/utxo"
        response = requests.get(utxos_url)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        utxos = response.json()

        txid = utxos
        vout = 1
        
        await asyncio.sleep(1)
        # all amounts are needed to sign a taproot input
        # (depending on sighash)
        first_amount = to_satoshis(amount)
        amounts = [first_amount]

        # all scriptPubKeys are needed to sign a taproot input
        # (depending on sighash) but always of the spend input
        first_script_pubkey = fromAddress.to_script_pub_key()

        # alternatively:
        # first_script_pubkey = Script(['OP_1', pub.to_taproot_hex()])

        utxos_script_pubkeys = [first_script_pubkey]

        toAddress = P2pkhAddress(addr_to)

        # create transaction input from tx id of UTXO
        txin = TxInput(txid, vout)

        # create transaction output
        txOut = TxOutput(to_satoshis(gasfee), toAddress.to_script_pub_key())

        # create transaction without change output - if at least a single input is
        # segwit we need to set has_segwit=True
        tx = Transaction([txin], [txOut], has_segwit=True)
      
        # sign taproot input
        # to create the digest message to sign in taproot we need to
        # pass all the utxos' scriptPubKeys and their amounts
        sig = priv.sign_taproot_input(tx, 0, utxos_script_pubkeys, amounts)
       
        tx.witnesses.append(TxWitnessInput([sig]))

        # print raw signed transaction ready to be broadcasted
        print("\nRaw signed transaction:\n" + tx.serialize())

        # Broadcast the transaction using Blockstream's API
        broadcast_url = "https://blockstream.info/testnet/api/tx"
        response = requests.post(broadcast_url, data= tx.serialize())

        # Check if the broadcast was successful
        if response.status_code == 200:
            return {"message": "Transaction broadcasted successfully"}
        else:
            return {"error": "Failed to broadcast transaction"}
        print("\nTxId:", tx.get_txid())
        print("\nTxwId:", tx.get_wtxid())

        print("\nSize:", tx.get_size())
        print("\nvSize:", tx.get_vsize())

        return{
            "Raw transaction": tx.serialize(),
            "txid":  tx.get_txid(),
            "txwid": tx.get_wtxid()
            }
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": str(e)}



