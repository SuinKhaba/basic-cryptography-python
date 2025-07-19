#!/bin/bash
# Run: chmod +x openssl_demo.sh && ./openssl_demo.sh

# AES Encryption 
echo "HelloWorld! My Name is SuinKhaba" > plain.txt
openssl enc -aes-256-cbc -salt -in plain.txt -out encrypted.txt -k secret123
openssl enc -d -aes-256-cbc -in encrypted.txt -out decrypted.txt -k secret123

# Generate RSA Keys
openssl genrsa -out private.pem 2048
openssl rsa -in private.pem -outform PEM -pubout -out public.pem
