#login system password with limit
import time as t

default_username = "kent".lower()
default_password = "tnek".lower()
correct = True
login_limit = 3
login_count = 1

def mainpage():
    for numberp in range(10):
        print(numberp)

while correct:
    name = input("Enter Username: ")
    pw = input("Enter Password: ")
    if name == default_username and pw == default_password:
        if login_count != login_limit:
            print("You have successfully logged in!")
            print("Directing to the main page")
            t.sleep(5)
            correct = False
            mainpage()
    elif name == default_username and pw != default_password:
        if login_count != login_limit:
            print("Wrong password please try again: ")
            rleft = login_limit - login_count
            login_count += 1
            print("Number of retries: " + str(rleft))
            correct = True
        elif login_count == login_limit:
            print("Error code retries, Max retries reached")
    elif name != default_username and pw == default_password:
        if login_count != login_limit:
            print("Wrong Username please try again: ")
            rleft = login_limit - login_count
            login_count += 1
            print("Number of retries: " + str(rleft))
            correct = True
        elif login_count == login_limit:
            print("Error code retries, Max retries reached")
    else:
        if login_count != login_limit:
            print("Wrong username and password please try again: ")
            rleft = login_limit - login_count
            login_count +=1
            print("Number of retries: " + str(rleft))
            correct = True
        elif login_count == login_limit:
            print("Error code retries, Max retries reached")
  