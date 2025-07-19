from aes_crypto import aes_menu
from rsa_crypto import rsa_menu
from sha_hash import sha_menu

def main():
    while True:
        print("\nChoose encryption method:")
        print("1. AES")
        print("2. RSA")
        print("3. SHA Hash")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            aes_menu()
        elif choice == '2':
            rsa_menu()
        elif choice == '3':
            sha_menu()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
