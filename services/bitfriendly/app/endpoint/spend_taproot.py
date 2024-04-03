from bitcoinutils.keys import P2shAddress, PrivateKey
from bitcoinutils.script import Script
from bitcoinutils.setup import setup
from bitcoinutils.hdwallet import HDWallet
from bitcoinutils.transactions import Transaction, TxInput, TxOutput, TxWitnessInput

setup("testnet")

#
# Send from a P2SH(P2WSH(P2PK)) UTXO to a P2PKH UTXO
#

xprivkey = (
    "tprv8ZgxMBicQKsPdQR9RuHpGGxSnNq8Jr3X4WnT6Nf2eq7FajuXyBep5KWYpYEixxx5XdTm1N"
    "tpe84f3cVcF7mZZ7mPkntaFXLGJD2tS7YJkWU"
)
path = "m/86'/1'/0'/0/20"
hdw = HDWallet(xprivkey, path)
from_priv = hdw.get_private_key()
print(from_priv.to_wif())
from_pub = from_priv.get_public_key()
from_addr = from_pub.get_address()

witness_script = Script([from_pub.to_hex(), "OP_CHECKSIG"])
p2sh_redeem_script = witness_script.to_p2wsh_script_pub_key()
print("From address:", P2shAddress.from_script(p2sh_redeem_script).to_string())

hdw.from_path("m/86'/1'/0'/0/20")
to_priv = hdw.get_private_key()
to_address = to_priv.get_public_key().get_address()
print("To address:", to_address.to_string())

# UTXO's info
txid = "217f123726bd8ace101afd705ae31384fd818fce17c8e00ce6fc0d24c0364355"
vout = 0
amount = 5000

txin = TxInput(txid, vout)
txout = TxOutput(3000, to_address.to_script_pub_key())
tx = Transaction([txin], [txout], has_segwit=True)

sig = from_priv.sign_segwit_input(tx, 0, witness_script, amount)

txin.script_sig = Script([p2sh_redeem_script.to_hex()])
tx.witnesses.append(TxWitnessInput([sig, witness_script.to_hex()]))

signed_tx = tx.serialize()

print(signed_tx)


#!/usr/bin/env python3

from hdwallet import HDWallet
from hdwallet.utils import generate_entropy
from hdwallet.symbols import BTC as SYMBOL
from typing import Optional

import json

# Choose strength 128, 160, 192, 224 or 256
STRENGTH: int = 128  # Default is 128
# Choose language english, french, italian, spanish, chinese_simplified, chinese_traditional, japanese or korean
LANGUAGE: str = "english"  # Default is english
# Generate new entropy hex string
ENTROPY: str = generate_entropy(strength=STRENGTH)
# Secret passphrase for mnemonic
PASSPHRASE: Optional[str] = None  # "meherett"

# Initialize Bitcoin mainnet HDWallet
hdwallet: HDWallet = HDWallet(symbol=SYMBOL, use_default_path=False)
# Get Bitcoin HDWallet from entropy
hdwallet.from_entropy(
    entropy=ENTROPY, language=LANGUAGE, passphrase=PASSPHRASE
)

# Derivation from path
hdwallet.from_path("m/44'/0'/0'/0/20")

print(json.dumps(hdwallet.dumps(), indent=4, ensure_ascii=False))

# Copyright (C) 2018-2022 The python-bitcoin-utils developers
#
# This file is part of python-bitcoin-utils
#
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution.
#
# No part of python-bitcoin-utils, including this file, may be copied,
# modified, propagated, or distributed except according to the terms contained
# in the LICENSE file.


from bitcoinutils.setup import setup
from bitcoinutils.utils import to_satoshis
from bitcoinutils.transactions import Transaction, TxInput, TxOutput
from bitcoinutils.keys import P2pkhAddress, PrivateKey
from bitcoinutils.script import Script


def main():
    # always remember to setup the network
    setup("testnet")

    #
    # This script spends from a P2SH address containing a P2PK script
    #

    # create transaction input from tx id of UTXO (contained 0.1 tBTC)
    txin = TxInput(
        "7db363d5a7fabb64ccce154e906588f1936f34481223ea8c1f2c935b0a0c945b", 0
    )

    # secret key needed to spend P2PK that is wrapped by P2SH
    p2pk_sk = PrivateKey("cRvyLwCPLU88jsyj94L7iJjQX5C2f8koG4G2gevN4BeSGcEvfKe9")
    p2pk_pk = p2pk_sk.get_public_key().to_hex()
    # create the redeem script - needed to sign the transaction
    redeem_script = Script([p2pk_pk, "OP_CHECKSIG"])

    to_addr = P2pkhAddress("n4bkvTyU1dVdzsrhWBqBw8fEMbHjJvtmJR")
    txout = TxOutput(to_satoshis(0.09), to_addr.to_script_pub_key())

    # no change address - the remaining 0.01 tBTC will go to miners)

    # create transaction from inputs/outputs -- default locktime is used
    tx = Transaction([txin], [txout])

    # print raw transaction
    print("\nRaw unsigned transaction:\n" + tx.serialize())

    # use the private key corresponding to the address that contains the
    # UTXO we are trying to spend to create the signature for the txin -
    # note that the redeem script is passed to replace the scriptSig
    sig = p2pk_sk.sign_input(tx, 0, redeem_script)
    # print(sig)

    # set the scriptSig (unlocking script)
    txin.script_sig = Script([sig, redeem_script.to_hex()])
    signed_tx = tx.serialize()

    # print raw signed transaction ready to be broadcasted
    print("\nRaw signed transaction:\n" + signed_tx)
    print("\nTxId:", tx.get_txid())
