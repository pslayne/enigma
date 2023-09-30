import numpy
from random import randbytes 
import hashlib

def generate_key(size):
    # generate a random key with the exact size of the msg
    return randbytes(size)

def xor(a, b):
    result_int = int.from_bytes(a, byteorder="big") ^ int.from_bytes(b, byteorder="big")
    return result_int.to_bytes(max(len(a), len(b)), byteorder="big")


def max_size(img_shape):
    # receives the shape of the numpy array that represents the img
    # calculates the maximum size of the msg this img can hide
    pass

def hash(cipher, max_size):
    # hashes the cipher
    pass

def encrypt(msg):
    try:
        assert type(msg) == type('str')
    except AssertionError:
        print('encrypt function expects a string')
    # get a key
    key = generate_key(len(msg))
    # msg xor key
    encrypted_msg = xor(msg.encode(), key)
    return encrypted_msg, key
    # returns the combined hash

def decrypt(cipher, key): # remove the key
    # receives the hash of the cipher msg and the key combined
    # "dehash" and decipher
    # returns the plain text
    return xor(cipher, key)

