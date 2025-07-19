from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def pad(text):
    return text + (16 - len(text) % 16) * chr(16 - len(text) % 16)

def unpad(text):
    return text[:-ord(text[-1])]

def aes_encrypt(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return base64.b64encode(cipher.encrypt(pad(data).encode())).decode()

def aes_decrypt(enc_data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return unpad(cipher.decrypt(base64.b64decode(enc_data)).decode())

def aes_menu():
    key = get_random_bytes(16)  # 128-bit AES key
    print(f"\nAES Key: {key.hex()}")

    text = input("Enter data to encrypt: ")
    encrypted = aes_encrypt(text, key)
    print(f"Encrypted: {encrypted}")

    decrypted = aes_decrypt(encrypted, key)
    print(f"Decrypted: {decrypted}")
