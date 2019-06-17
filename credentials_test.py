import unittest
import credentials


class TestCredentials(unittest.TestCase):
    """
    Test class that defines test cases for Credentials class behaviours

    Args:
        unittest.TestCase: TestCase class that helps in creates test cases
    """

    def setUp(self):
        """
        Setup method to run before each test cases
        """
        self.new_credentials = Credentials("Dinos", "WeChat", "dinos254", "pass12345")

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_credentials.first_name, "Dinos")
        self.assertEqual(self.new_credentials.last_name, "Gianis")
        self.assertEqual(self.new_credentials.user_name, "Dinos254")
        self.assertEqual(self.new_credentials.password, 'pass12345')


if __name__ == '__main__':
    unittest.main()
