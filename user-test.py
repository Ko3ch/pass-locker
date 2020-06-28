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
        '''
        test case to check whether User is instanciating
        '''
        self.assertEqual(self.new_user.user_name, "tom")
        self.assertEqual(self.new_user.password, "890000")
        self.assertEqual(self.new_user.credentials, Credentials.acc_details)

    def test_add_user(self):
        '''
        test case for add_user()
        '''
        self.new_user.add_user()

    def test_save_user_credentials(self):
        '''
        test case to check if credentials are being added successfully
        '''
        self.assertEqual(self.new_user.credentials, Credentials.acc_details)

    def test_user_exists(self):
        '''
        test case to check if a user exists 
        '''
        self.test_user = User("Test","0000",'')
        self.test_user.add_user()
        user_exists = User.user_exists("Test")

        self.assertTrue(user_exists)

    def test_diplay_users(self):
        '''
        test case to check if we can view all users 
        '''
        self.new_user.add_user()
        self.assertEqual(User.display_users(), User.users)

    def test_find_user_by_name(self):
        '''
        test case to check if we can find a user by their user_name
        '''
        self.test_user = User("Test","0000",'')
        self.test_user.add_user()

        found_user = User.find_user_by_user_name("Test")

        self.assertEqual(self.test_user.user_name, found_user.user_name)
        
if __name__ == "__main__":
    unittest.main()