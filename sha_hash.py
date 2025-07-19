import hashlib

def sha_menu():
    text = input("\nEnter text to hash (SHA-256): ")
    hashed = hashlib.sha256(text.encode()).hexdigest()
    print(f"SHA-256 Hash: {hashed}")
