import random
import string

users_list = []

class User:
        '''
        Class to create an account and save user information
        '''
        users_list = []
        def __init__(self,fname,lname,pword):
           
            self.fname = fname
            self.lname = lname
            self.pword = pword

        def save_user(self):
            '''
            Function to save the user of the app's information
            '''
            User.users_list.append(self)

class Credential:
        '''
        Class to add account credentials, generate password, save the iformation and deletewhat they don't need anymore.
        '''
        credentials_list = []
        user_info_list = []

        @classmethod
        def verify_user(cls,fname,pword):
            '''
            Method to verify user's input .
            '''
            logged_in_user = ''
            for user in User.users_list:
                    if(user.fname == fname and user.pword == pword):
                        logged_in_user = user.fname
            return logged_in_user 

        def __init__(self,account_name,user_name,email,pword):
            '''
            Function toshow the details each user should have.
            '''
            self.account_name = account_name
            self.user_name = user_name
            self.email = email
            self.pword = pword

        def save_credentials(self):
            '''
            Function to save created credentials.
            '''
            Credential.credentials_list.append(self) 

        def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
            '''
            Generating a password with 8 characters
            '''
            gen_pw = ''.join(random.choice(char) for _ in range(size)) 
            return gen_pw
# _
        @classmethod
        def show_credentials(cls,user_name):
            '''
            Function to show thelit of credentials saved
            '''
            user_info_list = []
            for credential in cls.credentials_list:
                if credential.user_name == user_name:
                    user_info_list.append(credential)

            return user_info_list  

        @classmethod
        def find_account_info(cls,account_name):
            '''
            Method that helps user get account information.
            '''
            for credential in cls.credentials_list:
                if credential.account_name == account_name:
                    return credential   

      







