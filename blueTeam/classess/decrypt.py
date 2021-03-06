from cryptography.fernet import Fernet
import time, os
from .zipper import *

# decrypting the folder
def decryptFolder(dirNames, key):
    completeFileList = list()
    fer=Fernet(key)
    for (dirPath, dirName, fileName) in os.walk(dirNames):
        completeFileList += [os.path.join(dirPath, file) for file in fileName]
    for fil in completeFileList:
        if not ("key.key") in fil:
            print(fil)
            decryptFile(fil, key)


# decrypting the file
def decryptFile(file, key):
    f = Fernet(key)
    with open(file, "rb") as fileread:
        # read the encrypted data
        encrypted_data = fileread.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(file, "wb") as filewrite:
        filewrite.write(decrypted_data)
        time.sleep(1)
        print("file has been decrypted")