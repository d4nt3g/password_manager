from functions import *

while True:
    print("Password Manager \n Choose an option: \n (1) Add password /// (2) See passwords")
    option = input("")
    if option in ("1", "2"):
        if option == "1":
            name = input("Name: ")
            password = input("Password: ")
            addPassword(name, password)
        else:
            passwordName = input("Name: ")
            seePassword(passwordName)
    Continue = input("Continue? \n (y/n) ")
    if Continue in ("y", "n"):
        if Continue == "y":
            print("Ok\n")
        else:
            input("Press enter to close the application")
            break