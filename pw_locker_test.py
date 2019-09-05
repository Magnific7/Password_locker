import unittest
from user_credential import User
from user_credential import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    Args:
	    unittest.TestCase: helps in creating test cases
    '''
    def setUP(self):
        '''
        Function to create user account.
        '''
        self.new_user  = User('Mag','Um','SGhhn20m')

    def test__init__(self):
        '''
        Test to see if the initialisation works.
        '''
        self.new_user  = User('Mag','Um','SGhhn20m')

        self.assertEqual(self.new_user.fname,'Mag')
        self.assertEqual(self.new_user.lname,'Um') 
        self.assertEqual(self.new_user.pword,'SGhhn20m')

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user  = User('Mag','Um','SGhhn20m')

        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.users_list),1)

class TestCredential(unittest.TestCase):
    '''
    Tests for credential class functions and methods.
    Args:
        unittest.TestCase: helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up function to run before each test cases.
        '''
        self.new_credential = Credential('gmail','mjones','mjones6944@gmail.com','20ggJJyh')

    def test_verify_user(self):
        '''
        Test for the verify_user() function
        '''
        self.new_user = User('Mag','Um','SGhhn20m')
        self.new_user.save_user()
        user1 = User('Mwiin','sick','SGhhn20m')
        user1.save_user()
        logged_in_user = ''

        for user in User.users_list:
            if user.fname == user1.fname and user.pword == user.pword:
                logged_in_user = user.fname
            return logged_in_user

            self.assertEqual(logged_in_user,Credential.verify_user(user1.pword,user1.fname))    
    

if __name__ == '__main__':
    unittest.main()
             

    