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
    return random_password


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
            print(f'Account succesfully created, username {user_name}, password {password}.')
        elif short_code == "li":
            print("")
            print("-"*100)
            print("Log In with your username and password:")
            user_name = input("Enter your username:")
            password = input("Enter your password")
