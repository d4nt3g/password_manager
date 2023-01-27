listA = []
listB = []

print("Password Manager \n Choose an option: \n (1) Add password /// (2) See passwords")
option = input("")
if option == "1":
    passwords = open("passwords.txt", "a")
    passwordsNames = open("passwordsNames.txt", "a")
    passwordName = input("Enter Password Name: ")
    password = input("Enter Password: ")
    listA.extend([password, "\n"])
    passwords.writelines(listA)
    listB.extend([passwordName, "\n"])
    passwordsNames.writelines(listB)
    passwords.close()
    passwordsNames.close()
if option == "2":
    passwords = open("passwords.txt", "r")
    passwordsNames = open("passwordsNames.txt", "r")
    lines = len(passwordsNames.readlines())
    name = input("Password Name write ['(Password Name)']: ")
    for x in range(lines):
        print(passwordsNames.readlines(x))