#!/usr/bin/env python3.6
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
    User.save_user()

def check_user(fname,pword):
    '''
    Function checks if a user exists
    '''
    checking_user = Credential.verify_user(fname,password)
    return checking_user



