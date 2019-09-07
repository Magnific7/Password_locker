import unittest
from user_credential import User
from user_credential import Credential

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

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.users_list = []   

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

        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)

class TestCredential(unittest.TestCase):
    '''
    Tests for credential class functions and methods.
    Args:
        unittest.TestCase: helps in creating test cases
    '''
    def test__init__(self):
        '''
        Test for the initialisation of the created credentials.
        '''
        self.assertEqual(self.new_credential.account_name,'gmail')
        self.assertEqual(self.new_credential.user_name,'mjones')
        self.assertEqual(self.new_credential.email,'mjones6944@gmail.com')
        self.assertEqual(self.new_credential.pword,'SGhhn20m')

    def setUp(self):
        '''
        Set up function to run before each test cases.
        '''
        self.new_credential = Credential('gmail','mjones','mjones6944@gmail.com','SGhhn20m')

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credential.credentials_list = []    

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

    def test_save_credentials(self):
        '''
        Test for the saving of credentials.
        '''
        self.new_credential.save_credentials()
        instagram = Credential('Instagram','Mag','mag@instagram.com','SGhhn20m')
        instagram.save_credentials()
        self.assertEqual(len(Credential.credentials_list),2)

    def test_show_credentials(self):
        '''
        Test for the show_credentials method.
        '''
        self.new_credential.save_credentials()
        instagram = Credential('Instagram','Mag','mag@instagram.com','SGhhn20m')
        instagram.save_credentials()
        github =Credential('github','Mag','mjones6944@gmail.com','SGhhn20m')
        github.save_credentials()
        self.assertEqual(len(Credential.show_credentials(instagram.user_name)),2)

    def test_find_account_info(self):
        '''
        Test to find account credentials by accountname.
        '''
        self.new_credential.save_credentials()
        instagram = Credential('Instagram','Mag','mag@instagram.com','SGhhn20m')
        instagram.save_credentials()
        credential_exists = Credential.find_account_info('Instagram')
        self.assertEqual(credential_exists,instagram)

    def test_copy_credential(self):
		'''
		Test to check if the copy a credential method copies the correct credential
		'''
		self.new_credential.save_credentials()
		instagram = Credential('Instagram','Mag','mag@instagram.com','SGhhn20m')
		instagram.save_credentials()
		find_credential = None
		for credential in Credential.user_credentials_list:
				find_credential =Credential.find_account_info(credential.account_name)
				return pyperclip.copy(find_credential.pword)
		Credential.copy_credential(self.new_credential.account_name)
		self.assertEqual('SGhhn20m',pyperclip.paste())
		print(pyperclip.paste())                    
    

if __name__ == '__main__':
    unittest.main()
             

    