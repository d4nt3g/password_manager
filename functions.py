import linecache
def addPassword(n,p):
    with open("passwordsNames.txt", 'a') as wn:
        wn.write(n)
        wn.write("\r")
    with open("passwords.txt", 'a') as wp:
        wp.write(p)
        wp.write("\r")
def seePassword(n):
    with open("passwordsNames.txt", 'r') as rn:
        line_num = 0
        for line_num, line in enumerate(rn, 1):
            if "%s\n" % n in line :
                print(f"Your {n} password is:")
                break
        password = linecache.getline("passwords.txt", line_num)
        print(password)