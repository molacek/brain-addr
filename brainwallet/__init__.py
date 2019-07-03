import hashlib
import getpass
import sys
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress


def sha256_pass(pwd, n=1):
    """ Hash the input n-times"""
    h = hashlib.sha256(pwd.encode('ascii'))
    for x in range(0, n-1):
        h = hashlib.sha256(h.digest())
    return h.digest()


def main():
    pwd = getpass.getpass("Enter your pwd: ")
    if pwd != getpass.getpass("Confirm your pwd: "):
        print("Error: Passwords dont match!")
        sys.exit()

    iter_text = input("Number of iterations: ")
    try:
        iterations = int(iter_text)
    except ValueError:
        print("Error converting to number")
        sys.exit()

    priv_key_hash = sha256_pass(pwd, iterations)
    priv_key = CBitcoinSecret.from_secret_bytes(priv_key_hash)
    pub_addr = P2PKHBitcoinAddress.from_pubkey(priv_key.pub)

    print(priv_key)
    print(pub_addr)

