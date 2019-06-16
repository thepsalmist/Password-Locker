from user import User
import string
import random


class Credentials:
    """
    Class to create and store user credentials
    """
    user_credential = []

    def __init__(self, website, username, account_name, password):
        """
        Method to create instances of class Credentials
        """
        self.website = website
        self.username = username
        self.account_name = account_name
        self.password = password

    def save_credentials(self):
        """
        Function that saves new credentials instances
        """
        Credentials.user_credential.append(self)
