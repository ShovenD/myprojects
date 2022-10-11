from pickle import TRUE


master_pwd= input("what is the master password:- ")

def view():
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            data=line.rstrip()
            user ,Passwd = data.split("|")
            print("User:", user, ",Password:", Passwd)

def add():
    name =input("Account name:-  ")
    pwd = input("Password:-  ")

    with open('passwords.txt','a') as f:
        f.write(name + "|"+ pwd+"\n")



while TRUE:
    mode = input("Would you like to add a new password or use existing password(view,add)? press q to quit? :- ")
    if mode =="q":
        break

    if mode =="view":
        view()

    elif mode =="add":
        add()

    else:
        print("Invalid mode.")
        continue