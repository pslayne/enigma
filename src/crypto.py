from random import randbytes 

def generate_key(size):
    # generate a random key with the exact size of the msg
    return randbytes(size)

def xor(a, b):
    result_int = int.from_bytes(a, byteorder="big") ^ int.from_bytes(b, byteorder="big")
    return result_int.to_bytes(max(len(a), len(b)), byteorder="big")

def encrypt(msg):
    try:
        assert type(msg) == type('str')
    except AssertionError:
        print('encrypt function expects a string')
    
    key = generate_key(len(msg))
    encrypted_msg = xor(msg.encode(), key)
    size = (len(key) * 2).to_bytes(4, byteorder='big')
    print(len(key) * 2)
    print(size)
    concat = size + key + encrypted_msg
    return concat

def decrypt(cipher, size):
    key = cipher[:size]
    msg = cipher[size:]
    plain = xor(msg, key).decode()
    return plain

