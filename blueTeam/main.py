#======= Library ========#
from time import sleep
import socket,sys,os
from cryptography.fernet import Fernet
from classess.encrypt import *
from classess.decrypt import *
from classess.remove_files import *
from classess.blockIt import *
from classess.zipper import *
from classess.openIt import *

#======= Variables ========#
keyLocation = "./key.key"

#======= Function =========#
# display interface
def interface(keys):
    print("""
    ________      _____               ______     __________ 
    ___  __/_________(_)_________________  /________(_)_  /_
    __  /  __  ___/_  /__  ___/__  __ \_  /_  __ \_  /_  __/
    _  /   _  /   _  / _(__  )__  /_/ /  / / /_/ /  / / /_  
    /_/    /_/    /_/  /____/ _  .___//_/  \____//_/  \__/  
                               /_/                           
                            version 1.0

    1) Encrypt Folder & Zip
    2) UnZip file
    3) Decrypt Folder
    4) Open port
    5) Close port
    6) Exit
    """)
    userInput = input("Enter your choice... ")
    if(userInput == "1"):
        ## encryption method
        userFolder=input("What folder do you want to input ")
        userFolder=f"./{userFolder}"
        encrptFolder(userFolder, keys)
        remove_file(keyLocation)
        remove_folder(userFolder)
    elif(userInput == "2"):
        ## Decryption method
        zipFolder=input("What file do you want to unzip? ")
        zipFolder=f"./{zipFolder}"
        extractFile(zipFolder)
    elif(userInput == "3"):
        ## Decryption method
        userFolder=input("What folder do you want to input ")
        userFolder=f"./{userFolder}"
        decrypt_key = get_key(f"{userFolder}/key.key") 
        decryptFolder(userFolder, decrypt_key)
    elif(userInput == "4"):
        ## open the port
        port_number = input("What port would you like to open? ")
        add_rule_allow(int(port_number))
    elif(userInput == "5"):
        ## close the port
        port_number = input("What port would you like to block? ")
        add_rule(int(port_number))

    else:
        ## exit
        if(os.path.isfile(keyLocation)):
            remove_file(keyLocation)
        print("Exiting...")
        sleep(1)
        exit()

#====== Key functions =======#
# getting the key
def get_key(keyLocations):
    return open(keyLocations, "rb").read()
# creating the key 
def generate_key():
    key = Fernet.generate_key()
    with open(keyLocation, "wb") as key_file:
        key_file.write(key)

#======= main ========#
def main():
    ## creating the key
    generate_key()
    ## Get the key
    key=get_key(keyLocation)
    while True:
        interface(key)
        
if __name__ == "__main__":
    main()

#======== END ==========#