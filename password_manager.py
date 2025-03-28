## Password Manager
master_pwd = print("What is the master Password. ")

def view():
    with open('Password.txt','r') as f:
        for line in f.readlines():
            data = (line.rstrip())
            user,passw = data.split("|")
            print(f"User:{user} | Password:{passw}")

def add():
    name = input("Account Name.: ")
    pwd = input("Password.: ")
    
    with open('Password.txt','a') as f:
        f.write(name + "|" + pwd + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones(view,add)? ").lower()
    if mode == "view":
        view()
        break
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue
    
    