import unittest
from credentials import Credentials
from user import User

class TestUser(unittest.TestCase):
    '''
    Provides test cases for user class
    '''
    def setUp(self):
        '''
        setup method to run before each test cases
        '''
        self.new_user = User("tom","890000",Credentials.acc_details)
        self.new_user.add_user()

    def test_instance(self): 
        self.assertEqual(self.new_user.user_name, "tom")
        self.assertEqual(self.new_user.password, "890000")
        self.assertEqual(self.new_user.credentials, Credentials.acc_details)

    def test_add_user(self):
        self.new_user.add_user()

    def test_save_user_credentials(self):
        self.assertEqual(self.new_user.credentials, Credentials.acc_details)

    def test_user_exists(self):
        self.test_user = User("Test","0000",'')
        self.test_user.add_user()
        user_exists = User.user_exists("Test")

        self.assertTrue(user_exists)

    def test_diplay_users(self):
        self.new_user.add_user()
        self.assertEqual(User.display_users(), User.users)

    def test_find_user_by_name(self):
        self.test_user = User("Test","0000",'')
        self.test_user.add_user()

        found_user = User.find_user_by_user_name("Test")

        self.assertEqual(self.test_user.user_name, found_user.user_name)
        
if __name__ == "__main__":
    unittest.main()