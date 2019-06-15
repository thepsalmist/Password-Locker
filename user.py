class User:
    """
    Class to create new user accounts
    """

    def __init__(self, first, last):
        """
        Method to create instances of class User
        """
        self.first = first
        self.last = last
        self.username = '@' + first
        self.email = first + '.' + last + '@gmail.com'
