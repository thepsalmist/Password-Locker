from user import User
from credentials import Credentials


def create_account(first_name, last_name, password):
    """
    Fuction that creates a new user account when a user opts to sign-up
    """
    new_user = User(first_name, last_name, password)
    return new_user


def save_account(user):
    """
    Function to save a new user account on sign-up
    """
    User.save_user(user)


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
            password = input("Enter Your Password")
            save_account(create_account(first_name, last_name, password))
            print("-"*10)
            print(f'Account succesfully created, username {username}, password {password}.')
        elif short_code == "li":
            print("")
            print("-"*100)
            print("Log In with your username and password:")
