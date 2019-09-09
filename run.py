#!/usr/bin/env python3.6
import pyperclip
from user_credential import User
from user_credential import Credential

def create_user(fname,lname,pword):
    '''
    Function to create a new user
    '''
    new_user = User(fname,lname,pword)
    return new_user

def save_user(user):
    '''
    Function to save a new user account
    '''
    User.save_user(user)

def verify_user(fname,pword):
    '''
    Function checks if a user exists
    '''
    checking_user = Credential.verify_user(fname,pword)
    return checking_user

def generate_password():
    '''
    Function to generate a password.
    '''
    gen_pw = Credential.generate_password()
    return gen_pw

def create_credential(user_name,email,account_name,pword):
	'''
	Function to create a new credential
	'''
	new_credential=Credential(user_name,email,account_name,pword)
	return new_credential

def save_credential(credential):
	'''
	Function to save a newly created credential
	'''
	Credential.save_credentials(credential)

def show_credentials(user_name):
	'''
	Function to show credentials saved by a user
	'''
	return Credential.show_credentials(user_name)
	
def copy_credential(email):
	'''
	Function to copy a credentials details to the clipboard
	'''
	return Credential.copy_credential(email)

def main():
	print(' ')
	print('Hello! Welcome to Password Locker.')
	while True:
		print(' ')
		print("-"*60)
		print('Use these codes to navigate: \n ca-Create an Account \n li-Log In \n ex-Exit')
		short_code = input('Enter a choice: ').lower().strip()
		if short_code == 'ex':
			break

		elif short_code == 'ca':
			print("-"*60)
			print(' ')
			print('To create a new account:')
			fname = input('Enter your first name - ').strip()
			lname = input('Enter your last name - ').strip()
			pword = input('Enter your password - ').strip()
			save_user(create_user(fname,lname,pword))
			print(" ")
			print(f'New Account Created for: {fname} {lname} using password: {pword}')
		elif short_code == 'li':
			print("-"*60)
			print(' ')
			print('To login, enter your account details:')
			user_name = input('Enter your first name - ').strip()
			pword = str(input('Enter your password - '))
			user_exists = verify_user(user_name,pword)
			if user_exists == user_name:
				print(" ")
				print(f'Welcome {user_name}. Please choose an option to continue.')
				print(' ')
				while True:
					print("-"*60)
					print('Navigation codes: \n cc-Create a Credential \n dc-show Credentials \n ex-Exit')
					short_code = input('Enter a choice: ').lower().strip()
					print("-"*60)
					if short_code == 'ex':
						print(" ")
						print(f'Goodbye {user_name}')
						break
					elif short_code == 'cc':
						print(' ')
						print('Enter your credential details:')
						email = input('Enter your user name.- ').strip()
						account_name = input('Enter the site\'s name - ').strip()
						while True:
							print(' ')
							print("-"*60)
							print('Please choose an option for entering a password: \n ep-enter existing password \n gp-generate a password \n ex-exit')
							psw_choice = input('Enter an option: ').lower().strip()
							print("-"*60)
							if psw_choice == 'ep':
								print(" ")
								pword = input('Enter your password: ').strip()
								break
							elif psw_choice == 'gp':
								pword = generate_password()
								break
							elif psw_choice == 'ex':
								break
							else:
								print('Oops! Wrong option entered. Try again.')
						save_credential(create_credential(user_name,email,account_name,pword))
						print(' ')
						print(f'Credential Created: user Name: {email} - Account Name: {account_name} - Password: {pword}')
						print(' ')
					elif short_code == 'dc':
						print(' ')
						if show_credentials(user_name):
							print('Here is a list of all your credentials')
							print(' ')
							for credential in show_credentials(user_name):
								print(f'user Name: {credential.email} - Account Name: {credential.account_name} - Password: {credential.pword}')
							print(' ')	
						else:
							print(' ')
							print("You don't seem to have any credentials saved yet")
							print(' ')
					# elif short_code == 'copy':
					# 	print(' ')
					# 	chosen_site = input('Enter the site name for the credential password to copy: ')
					# 	copy_credential(chosen_site)
					# 	print('')
					else:
						print('Oops! Wrong option entered. Try again.')

			# else: 
			# 	print(' ')
			# 	print('Oops! Wrong details entered. Try again or Create an Account.')		
		
		else:
			print("-"*60)
			print(' ')
			print('Oops! Wrong option entered. Try again.')    

if __name__ == '__main__':

    main()
      


