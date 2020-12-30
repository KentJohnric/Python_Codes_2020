#login system password with limit and in function
import time as t

default_username = "kent".lower()
default_password = "tnek".lower()
sysT = True

def mainpage():
    for numberp in range(10):
        print(numberp)
        t.sleep(1)

def errorpage(maxre):
    while maxre:
        print("Max retries reached, please stop the app")
        t.sleep(1)

def prompt():
    login_count = 1
    login_limit = 3
    sysT = True
    while sysT:
        name = input("Enter Username: ")
        pw = input("Enter Password: ")
        if name == default_username and pw == default_password:
            if login_count != login_limit:
                print("You have successfully logged in!")
                print("Directing to the main page")
                t.sleep(5)
                mainpage()
        elif name == default_username and pw != default_password:
            if login_count != login_limit:
                print("Wrong password please try again: ")
                rleft = login_limit - login_count
                login_count += 1
                print("Number of retries: " + str(rleft))
                sysT = True
            elif login_count == login_limit:
                print("Error code retries, Max retries reached")
                maxr = True
                errorpage(maxr)
        elif name != default_username and pw == default_password:
            if login_count != login_limit:
                print("Wrong Username please try again: ")
                rleft = login_limit - login_count
                login_count += 1
                print("Number of retries: " + str(rleft))
                sysT = True
            elif login_count == login_limit:
                print("Error code retries, Max retries reached")
                maxr = True
                errorpage(maxr)
        else:
            if login_count != login_limit:
                print("Wrong username and password please try again: ")
                rleft = login_limit - login_count
                login_count += 1
                print("Number of retries: " + str(rleft))
                sysT = True
            elif login_count == login_limit:
                print("Error code retries, Max retries reached")
                maxr = True
                errorpage(maxr)
prompt()