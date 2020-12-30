# basic login system password

correct = True
while correct:
    name = input("Enter Username: ")
    # .lower() makes the entered name to lower cases
    if name == "kent".lower():
        passw = input("Enter Password: ")
        if passw == "tnek".lower():
            print("You have successfully logged in")
        else:
            print("wrong password please try again")
            correct = True
    else:
        print("Wrong username please try again")
        correct = True
