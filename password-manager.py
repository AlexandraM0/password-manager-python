pwd = input ("What is the master password? ")

def view ()
    
    while True:
        mode = input (" Whould you like to add a new password or view existing ones? ")
        if mode == "q":
            break

        if mode == "view" :
            pass
        elif mode == "add":
            pass
        else:
            print("Invalid mode.")
            continue