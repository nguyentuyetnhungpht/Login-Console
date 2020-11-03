import csv

def main():
    f = open("account.txt", "r")
    file_reader = csv.reader(f)
    username_find(file_reader)
    f.close()

def username_find(file_account):
    username = input("Enter your username: ")
    for row in file_account:
        if row[0] == username:
            user_found = [row[0], row[1]]
            password_checked(user_found)
            break
        else:
            print("Username not found")
            break

def password_checked(user_found):
    password = input("Enter your password: ")
    if user_found[1] == password:
        print("Login success")
    else:
        print("Invalid password")


while True:
    print("************* LOGIN *************")
    print("*                               *")
    print("* 1. Login                      *")
    print("* 2. Register                   *")
    print("*                               *")
    print("*********************************")
    main()

