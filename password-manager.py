from cryptography.fernet import Fernet

master_pwd = input ("What is the master password? ")

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    return open ("key.key", "rb").read()


def view ():
    with open('password.txt', 'R') as f: 
      for line in f.readlines():
          data = (line.rstrip())
          user, passw = data.split("|")
          print("User:", user, "Password:", passw)

def add ():
    name = input ('Account Name: ')
    password = input ('Password: ')

    with open('password.txt', 'a') as f: 
        f.write(name + "|" + password + "\n")


while True:
    mode = input (" Whould you like to add a new password or view existing ones (view, add)? If you want to quit press q.").lower()
    if mode == "q":
        break

    if mode == "view" :
         view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue