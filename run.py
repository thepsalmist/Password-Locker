#! /usr/bin/en python3.6
from user import User
from credentials import Credentials


def create_account(first_name, last_name, user_name, password):
    """
    Fuction that creates a new user account when a user opts to sign-up
    """
    new_user = User(first_name, last_name, user_name, password)
    return new_user


def save_account(user):
    """
    Function to save a new user account on sign-up
    """
    User.save_user(user)


def create_credentials(website, user_name, account_name, password):
    """
    Function to create new user credentials
    """
    new_credentials = Credentials(website, user_name, account_name, password)
    return new_credentials


def store_credentials(credentials):
    """
    Function to store new user credentials
    """
    Credentials.save_credentials(credentials)


def display_credentials(user_name):
    """
    Function to display saved account credentials
    """
    return Credentials.display_credentials(user_name)


def delete_credentials(user_name):
    """
    Function to delete user credential
    """
    return Credentials.delete_credentials(user_name)


def auth_account(user_name, password):
    """
    Function to authenticate user accounts
    """
    authenticate_user = Credentials.auth_user(user_name, password)
    return authenticate_user


def create_password():
    """
    Function to create a random password for the users
    """
    new_password = Credentials.random_password()
    return new_password


def main():
    print(" ")
    print("WELCOME TO YOUR PASSWORD VAULT!!!")
    print("-"*100)
    while True:
        print(" ")
        print("Use the shortcodes below to navigate:\n 1. SU- Sign Up\n 2. LI- Log in to your\n 3. EX- Exit ")
        short_code = input("Short code:").lower()
        if short_code == "ex":
            print("-"*100)
            print("Thank You!")
            break

        elif short_code == "su":
            print(" ")
            print("-"*100)
            print("Fill in the details below to Sign-up for a new account:")
            first_name = input("First Name:")
            last_name = input("Last Name:")
            user_name = input("User Name:")
            password = input("Enter Your Password:")
            save_account(create_account(first_name, last_name, user_name, password))
            print("-"*10)
            print(f"Account succesfully created, username: {user_name}, password: {password}.")
        elif short_code == "li":
            print("")
            print("-"*100)
            print("Log in with your username and password:")
            user_name = input("Enter your username: ")
            password = input("Enter your password: ")
            valid_user = auth_account(user_name, password)
            if valid_user == user_name:
                print("-"*10)
                print(f"Welcome to password vault {user_name}. To proceed, pick one of the options below:")
                while True:
                    print("-"*100)
                    print("Use these short codes: \n 1. cc- Create new credentials \n 2. dc- Displaying saved credentials \n 3. dd- Delete credentials \n 4. ex- Exit ")
                    print(" ")
                    short_code = input("Enter short code:")
                    print("-"*10)
                    if short_code == "cc":
                        print(" ")
                        print("Enter account credentials:")
                        website = input("Website Name....")
                        account_name = input("User Account Name...")
                        print(" ")
                        print(
                            f"Thanks {account_name} Do you have an existing password? \n You can alternatively generate a new password below:")
                        while True:
                            print(" ")
                            print(
                                " Choose password option as below \n A- Enter existing password B- generate new password C-exit")
                            password_code = input("Password option:").lower()
                            if password_code == "a":
                                print(" ")
                                print("Enter you password:")
                                break
                            elif password_code == "b":
                                print(" ")
                                password = create_password()
                                break
                            elif password_code == "c":
                                break
                            else:
                                print("Kindly pick one of the options above!")
                        store_credentials(create_credentials(
                            website, user_name, account_name, password))
                        print("*"*10)
                        print(f"Account credentials saved as: Website {website}, Account name: {account_name} and Password: {password}")
                    elif short_code == "dc":
                        print(" ")
                        if display_credentials(user_name):
                            print("Your account credentials are as below:")
                            print("-"*100)
                            for credentials in display_credentials(user_name):
                                print(f"Website: {website}, Account Name: {account_name}, Password {password}")
                            print("-"*100)
                        else:
                            print(" ")
                            print("No credentials saved yet:")
                            print("-"*100)

                    elif short_code == "dd":
                        print(" ")
                        if delete_credentials(user_name):
                            print("Delete credential:")
                            for credentials in cls.account_credentials:
                                delete_credentials()
                            print("-"*100)
                        else:
                            print(" ")
                            print("No credentials saved yet:")
                            print("-"*100)
                    elif short_code == "ex":
                        print(" ")
                        print(f"Thank you {user_name} ,Bye!")
                        break
            else:
                print(" ")
                print("Sorry that account does not exist, please try again!")
                print("-"*100)


if __name__ == '__main__':
    main()
