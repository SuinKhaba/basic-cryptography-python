from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def rsa_menu():
    key = RSA.generate(2048)
    public_key = key.publickey()
    
    cipher = PKCS1_OAEP.new(public_key)
    text = input("\nEnter data to encrypt: ")
    enc = cipher.encrypt(text.encode())
    enc_b64 = base64.b64encode(enc).decode()
    print(f"Encrypted: {enc_b64}")

    cipher_dec = PKCS1_OAEP.new(key)
    decrypted = cipher_dec.decrypt(base64.b64decode(enc_b64)).decode()
    print(f"Decrypted: {decrypted}")
