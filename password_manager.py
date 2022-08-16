from cryptography.fernet import Fernet

'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("What is your master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            username, password = data.split("|")
            print("Username:", username, "Password:", fer.decrypt(password.encode()).decode())

def add():
    user = input("Account Username: ")
    pwd = input("Password: ")
    with open('passwords.txt', 'a') as f:
        f.write(user + " | " + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    option = input("View existing passwords or add new password? (view, add, quit)")
    if option == "quit":
        break
    if option == "view":
        view()
    elif option == "add":
        add()
    else:
        print("Invalid mode. Please choose view, add or quit.")
        continue 