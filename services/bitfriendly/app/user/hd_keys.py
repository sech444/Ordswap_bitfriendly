from bitcoinutils.setup import setup
from bitcoinutils.hdwallet import HDWallet

def main():
    # always remember to setup the network
    setup('Bitcoin')


    import secrets
    SECRET_KEY = secrets.token_hex(38)
    print(SECRET_KEY)
   
    # get an HDWallet wrapper object by extended private key and path
    xprivkey = "tprv8ZgxMBicQKsPdQR9RuHpGGxSnNq8Jr3X4WnT6Nf2eq7FajuXyBep5KWYpYEixxx5XdTm1Ntpe84f3cVcF7mZZ7mPkntaFXLGJD2tS7YJkWU"
    path = "m/86'/1'/0'/0/1"
    hdw = HDWallet(xprivkey, path)

    print('Ext. private key:', xprivkey)
    print('Derivation path:', path)

    # get a PrivateKey object used in bitcoinutils throughout
    privkey = hdw.get_private_key()
    print('WIF:', privkey.to_wif())

    # get public key
    pubkey = privkey.get_public_key()
    print('Pubkey:', pubkey.to_hex())

    # get legacy address
    addr1 = pubkey.get_address()
    print('Legacy address:', addr1.to_string() )

    # get segwit v0 address
    addr2 = pubkey.get_segwit_address()
    print('Segwit address:', addr2.to_string() )

    # get taproot (segwit v1) address
    addr3 = pubkey.get_taproot_address()
    print('Taproot address:', addr3.to_string() )

    new_path = "m/86'/1'/0'/0/5"
    hdw.from_path(new_path)
    print('\n\nNew derivation path:', new_path)

    # get a PrivateKey object used in bitcoinutils throughout
    privkey = hdw.get_private_key()
    print('WIF:', privkey.to_wif())

    # get public key
    pubkey = privkey.get_public_key()
    print('Pubkey:', pubkey.to_hex())

    # get legacy address
    addr1 = pubkey.get_address()
    print('Legacy address:', addr1.to_string() )

    # get segwit v0 address
    addr2 = pubkey.get_segwit_address()
    print('Segwit address:', addr2.to_string() )

    # get taproot (segwit v1) address
    addr3 = pubkey.get_taproot_address()
    print('Taproot address:', addr3.to_string() )





# import bech32
# import binascii
# import hashlib

# import hashlib
# import binascii
# from bech32 import bech32_encode, convertbits

# # This is your provided public key
# public_key = '034f6922d19e8134de23eb98396921c02cdcf67e8c0ff23dfd955839cd557afd10'

# # Perform SHA-256 hashing on the public key
# sha256 = hashlib.sha256(binascii.unhexlify(public_key)).digest()

# # Perform RIPEMD-160 hashing on the SHA-256 hash
# ripemd160 = hashlib.new('ripemd160')
# ripemd160.update(sha256)
# hash160 = ripemd160.digest()

# # Convert the hash160 to an array of 5-bit unsigned integers
# five_bit_pub_key = convertbits(hash160, 8, 5)

# # Witness version
# witver = 1

# # Encode the address
# address = bech32_encode('bc1p', [witver] + five_bit_pub_key)

# #print(address)

