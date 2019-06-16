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


def create_credentials(self, website, user_name, account_name, password):
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
            break

        elif short_code == "su":
            print(" ")
            print("-"*100)
            print("Fill in the details below to Sign-up for a new account:")
            first_name = input("First Name:")
            last_name = input("Last Name:")
            user_name = input("User Name:")
            password = input("Enter Your Password")
            save_account(create_account(first_name, last_name, user_name, password))
            print("-"*10)
            print(f"Account succesfully created, username: {user_name}, password: {password}.")
        elif short_code == "li":
            print("")
            print("-"*100)
            print("Log In with your username and password:")
            user_name = input("Enter your username: ")
            password = input("Enter your password: ")
            valid_user = auth_account(user_name, password)
            if valid_user == user_name:
                print("-"*10)
                print(f"Welcome to password vault {user_name}. To proceed, pick one of the options below:")
                print("*"*10 + "*"*10)
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
                            "Do you have an existing password? You can alternatively generate a new password below:")
                        while True:
                            print(" ")
                            print(
                                " Choose password option as below \n a- Enter existing password b- generate new password")
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
                    elif short_code == "dc":
                        print(" ")
                        if display_credentials(user_name):
                            print("Your account credentials are as below:")
                            print("-"*10)
                            for credentials in display_credentials(user_name):
                                print(f"Website: {website}, Account Name: {account_name}, Password {password}")
                            print("-"*10)
                        else:
                            print(" ")
                            print("No credentials saved yet:")
                            print("-"*10)

                    elif short_code == "dd":
                        print(" ")
                        if delete_credentials(user_name):
                            print("Delete credential:")
                            print("-"*10)
                            for credentials in cls.account_credentials:
                                delete_credentials()
                            print("-"*10)
                        else:
                            print(" ")
                            print("No credentials saved yet:")
                            print("-"*10)
                    elif short_code == "ex":
                        print(" ")
                        print(f"Thank you {user_name} ,Bye!")
                else:
                    print(" ")
                    print("Sorry that account does not exist, please try again!")
                    print("-"*10)
        elif short_code == "ex":
            break


if __name__ == '__main__':
    main()
