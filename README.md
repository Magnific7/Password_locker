# Password_locker
## Built By UM Magnific
## Description
Password Locker is a terminal run python application that allows users to store details i.e. usernames and passwords of their various accounts.
## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like:
* To create an account with my details - log in and password
* Store my existing login credentials
* Generate a password for a new credential/account

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display codes for navigation | **In terminal: $./run.py** | 
Welcome, choose an option: ca-Create Account, li-Log In, ex-Exit |
| Display prompt for creating an account | **Enter: ca** | Enter your first name, last name and password |
| Display prompt for login in | **Enter: li** | Enter your account name and password |
| Display codes for navigation | **Successful login** | Choose an option: cc - Create Credential, dc - Display Credentials, copy - Copy Credential, ex - exit |
| Display prompt for creating a credential | **Enter: cc** | Enter the site name, your username and password |
| Display a list of credentials | **Enter: dc** | Prints a list of saved credentials |
| Deleting a credential | **Enter: del** | prints out the site name ofthe deleted credential |
| Exit application | **Enter: ex** | Exit the current navigation stage |
## SetUp / Installation Requirements
### Prerequisites
* python3.6
### Assessing
* you need to clone the folder in your terminal
## Technologies Used
* Python3.6
## License
By UM Magnific 2019
