from functions import *

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