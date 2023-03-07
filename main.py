import json

while True:
    print("Password Manager \n Choose an option: \n (1) Add password /// (2) See passwords /// (3) Delete Password\n")
    option = input("")
    if option == "1":
        name = input("Name: ")
        password = input("Password: ")
        with open("passwords.json", "r+") as file:
            data = json.load(file)
            data[name] = password
            file.seek(0)
            json.dump(data, file)
    elif option == "2":
        name = input("Name: ")
        with open("passwords.json", "r") as file:
            data = json.load(file)
            try:
                print(f"Your {name} password is {data[name]}.\n")
            except KeyError:
                print(f"There's no password for {name}.")
    elif option == "3":
        name = input("Name: ")
        with open("passwords.json", "r") as file:
            data = json.load(file)
            del(data[name])
        with open("passwords.json", "w") as file:
            json.dump(data, file)
    else:
        print("Invalid")
        
    Continue = input("Continue? \n (y/n) ")
    if Continue in ("y", "n"):
        if Continue == "y":
            print("Ok\n")
        else:
            break