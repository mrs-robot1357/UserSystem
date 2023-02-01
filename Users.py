import random
import bcrypt
from constants import salt

#print(salt)
print("Hello! Welcome to our user management system!")
user_option = int(input("Would you like to: "
                        "1.Create an account? "
                        "2. Login to your account? "
                        "0. Exit application? "))


def create_account():
    while True:
        username = input('Please Enter your username: ')
        if username == '':
            print('Your username cannot be blank')
            continue
        passwd = input('Please enter your password: ')
        hashed = bcrypt.hashpw(passwd.encode('utf-8'), salt)
        hashed = hashed.decode('utf-8')
        if passwd == '':
            print("Your password can't be blank")
            continue
        if username != '' and passwd != '':
            print(f"Hi {username}! You have su"
                  f"ccessfully created an account.")
            database = open('UserFile.txt', 'a')
            l = f"{username}, {hashed},\n"
            database.writelines(l)
            database.close()
        break


def login():
    while True:
        with open('UserFile.txt', 'r') as database:
            # print(database.readlines())
            username = input('Please Enter your username: ')
            if username == '':
                print('Your username cannot be blank')
                continue
            password = input('Please enter your password: ')
            hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
            hashed = hashed.decode('utf-8')
            # print(password, hashed)
            if password == '':
                print("Your password can't be blank")
                continue
            for line in database.readlines():
                # print(line)
                uname, pwd = line.split(',')[0], line.split(',')[1]
            if username in uname:
                if hashed in pwd:
                    print(f"Hi {username}! Welcome to your account.")
                else:
                    print("Your password is incorrect.")
            else:
                print("We couldn't find your name in our database, sorry")

            break


while True:
    if user_option == 1:
        create_account()
        break

    elif user_option == 2:
        login()
        break

    elif user_option == 0:
        print("You have chosen to end this application, goodbye :(")
        break

    else:
        print("You have entered an invalid option.")
        break


