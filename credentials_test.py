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
        self.assertEqual(self.new_credentials.user_name, "Dinos")
        self.assertEqual(self.new_credentials.website, "WeChat")
        self.assertEqual(self.new_credentials.account_name, "dinos254")
        self.assertEqual(self.new_credentials.password, 'pass12345')

    def test_save_credentials(self):
        """
        Test to asertain that the new credentials are saved into the user_credentials list and check the user_credentials list length
        """
        self.new_credentials.save_credentials()
        Messenger = Credentials("Lalas", "Messenger", "lalas254", "papass12345")
        self.assertEqual(len(Credentials.user_credentials), 2)


if __name__ == '__main__':
    unittest.main()
