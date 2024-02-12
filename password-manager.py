pwd = input ("What is the master password? ")

def view ():
    pass



def add ():
    pass
    
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