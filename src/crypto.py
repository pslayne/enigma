import numpy 

def generate_key(size):
    # generate a random key with the exact size of the msg
    pass

def max_size(img_shape):
    # receives the shape of the numpy array that represents the img
    # calculates the maximum size of the msg this img can hide
    pass

def hash(cipher, max_size):
    # hashes the cipher
    pass

def encrypt(msg):
    # get a key
    # msg xor key
    # returns the combined hash
    pass

def decrypt(cipher):
    # receives the hash of the cipher msg and the key combined
    # "dehash" and decipher
    # returns the plain text
    pass

