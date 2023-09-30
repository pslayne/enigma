import crypto
import cv2 as cv

msg = 'hello, world!'
encrypted_msg, key = crypto.encrypt(msg)
decrypted_msg = crypto.decrypt(encrypted_msg, key)
print(encrypted_msg)
print(decrypted_msg.decode())