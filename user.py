class User:
    """
    Class to create new user accounts
    """
    users = []

    def __init__(self, first_name, last_name, password):
        """
        Method to create instances of class User
        """
        self.first = first_name
        self.last = last_name
        self.password = password
        self.username = '@' + first_name
        self.email = first_name + '.' + last_name + '@gmail.com'

    def save_user(self):
        """
        Function that saves new user instances
        """
        User.users.append(self)
