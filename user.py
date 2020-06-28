from credentials import Credentials
class User:
    users = []
    '''
    class that creates instances of a User
    '''
    def __init__(self, user_name, password, credentials):
        '''
        method to initialize User class
        '''
        self.user_name = user_name
        self.password = password
        self.credentials = []

    def add_user(self):
        '''
        method to add user to list of users
        '''
        User.users.append(self)  

    @classmethod
    def add_user_credentials(cls):
        '''
        method to add the accounts details of the user
        '''
        cls.credentials = Credentials.acc_details

    @classmethod
    def display_users(cls):
        '''
        method to get all users
        '''
        return cls.users

    @classmethod
    def find_user_by_user_name(cls, name):
        '''
        method that finds a user by user_name and returns the user
        '''
        for user in cls.users:
            if user.user_name == name:
                return user

    @classmethod
    def user_exists(cls, user_name):
        '''
        method that returns true if a user exists and false otherwise
        '''
        for user in cls.users:
            if user.user_name == user_name:
                return True
        
        return False




    