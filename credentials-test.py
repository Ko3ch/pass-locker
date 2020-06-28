import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    '''
    provide test cases to test Credentials class
    '''
    def setUp(self):
        self.new_account = Credentials("twitter","9000")
        self.new_account.save_acc_details()

    def test_instance(self):
        self.assertEqual(self.new_account.account_name, "twitter")
        self.assertEqual(self.new_account.account_password, "9000")

    def test_save_acc_details(self):
        self.new_account.save_acc_details()

    def test_delete_account(self):
        self.new_account.save_acc_details()
        self.test_account = Credentials("Test","User")
        self.test_account.save_acc_details()
        self.new_account.delete_acc_details()
        
        self.assertEqual(len(Credentials.acc_details),1)

    def test_find_account_by_name(self):
        self.test_user = Credentials("Test","0000")
        self.test_user.save_acc_details()

        found_account = Credentials.find_account_by_acc_name("Test")

        self.assertEqual(self.test_user.account_name, found_account.account_name)

if __name__ == "__main__":
    unittest.main()