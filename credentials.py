class Credentials():
    acc_details = []
    '''
    credentials class to create account details of a user
    '''
    def __init__(self, account_name, account_password):
        '''
        method that initializes the user's credentials
        '''
        self.account_name = account_name
        self.account_password = account_password

    def save_acc_details(self):
        '''
        method that adds accounts of a user
        '''
        Credentials.acc_details.append(self)

    def delete_acc_details(self):
        '''
        method that deletes a user's account
        '''
        Credentials.acc_details.remove(self)

    @classmethod
    def view_accounts(cls):
        '''
        method that displays al accounts a user has
        '''
        return cls.acc_details
    
    @classmethod
    def find_account_by_acc_name(cls, name):
        '''
        method that finds a user by user_name and returns the user
        '''
        for account in cls.acc_details:
            if account.account_name == name:
                return account