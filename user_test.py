import unittest
import user


class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for User class behaviours

    Args:
        unittest.TestCase: TestCase class that helps in creates test cases
    """

    def setUp(self):
        """
        Setup method to run before each test cases
        """
        self.new_user = User("Dinos", "Gianis", "Dinos254", "pass12345")

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user.first_name, "Dinos")
        self.assertEqual(self.new_user.last_name, "Gianis")
        self.assertEqual(self.new_user.user_name, "Dinos254")
        self.assertEqual(self.new_user.password, 'pass12345')


if __name__ == '__main__':
    unittest.main()
