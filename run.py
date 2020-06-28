#!/usr/bin/env python3
from user import User
from credentials import Credentials

def create_account(u_name, password, account_details):
    '''
    function to create new user account
    '''
    new_user = User(u_name,password,account_details)
    return new_user

def save_account(user):
    '''
    function to save users
    '''
    user.add_user()

def initialize():

    new_user = User("Test","User",'')
    return new_user

def check_account(user_name):
    '''
    function to check if account exists
    '''
    return User.user_exists(user_name)

def find_account(acc_name):
    '''
    find account by user_name
    '''
    return Credentials.find_account_by_acc_name(acc_name)

def all_users():
    '''
    function to get all users
    '''
    return User.display_users()

def create_user_credentials(account_name, account_password):
    '''
    function to create new credentials for a user
    '''
    new_user_credentials = Credentials(account_name, account_password)
    return new_user_credentials

def save_account_credentials(user,credentials):
    '''
    function to add user accounts details
    '''
    credentials.save_acc_details()
    user.add_user_credentials()
    

def delete_credentials(credentials):
    '''
    function to delete a users account credentials
    '''
    credentials.delete_acc_details()

def display_credentials():
    '''
    function tha returns all accounts saved by a user
    '''
    return Credentials.view_accounts()

def main():
    print("\n")
    print("Welcome to Password Locker")
    print("*" * 26)

    while True: 
        print("Use keys : ca - create new account : lg - login : ex : exit")
        key = input().lower()

        if key == "ca":
            print("**Create new account**")
            print("User-name: ")
            user_name = input()
            print("Password: ")
            password = input()
            print("\n")
            save_account(create_account(user_name,password,''))
            print("**Your account is ready --->, \n **lg to login")
            print("\n")

        elif key == "lg":
            print("**Login to your account now**")
            print("User-name: ")
            login_name = input()
            print("Password: ")
            login_password = input()
            print("\n")
            for user in all_users():
                if user.password == login_password and user.user_name == login_name:
                    print(f"Welcome {user.user_name}")
                    print("\n")
                    while True: 
                        print("\n")
                        print("Manage Accounts")
                        print("-"*15)
                        print("ac - add account : dc - delete account : va - view my accounts : ex - exit")
                        print("\n")

                        account = input().lower()
                        if account == "ac":
                            print("New account: ")
                            print("-"*15)
                            print("Account name: ")
                            acc_name = input()
                            print("Password: ")
                            passcode = input()
                            print("\n")
                            save_account_credentials(user,(create_user_credentials(acc_name,passcode)))

                            print(f"{acc_name} - {passcode}")
                            print("\n")

                        elif account == "dc":
                            print("Enter the account name: ")
                            name_acc_to_delete = input()
                            print("\n")
                            account_to_delete = find_account(name_acc_to_delete)
                            if account_to_delete:
                                delete_credentials(account_to_delete)
                                print("Deleted successfully")
                                print("\n")
                            
                            else:
                                print(f"There is no account by {name_acc_to_delete}")

                        elif account == "va":
                            if display_credentials():
                                print("My accounts")
                                print("*"*15)
                                print("Account Name    Password")
                                print("-"*25)
                                for account in display_credentials():
                                    print(f" {account.account_name}         {account.account_password}")
                            else:
                                print("\n")
                                print("You have no saved accounts")
                                print("\n")

                        elif account == "ex": 
                                break
                        else:
                            print("\n")
                            print("Invalid entry!! Try again")
                else:
                    print("Incorrect user-name/password")    
        elif account == "ex": 
            break    
        else:
            print("Invalid Input. Try again")
            print("\n")  

if __name__ == "__main__":
     main()
