import math
import string
import random

# Users list
users_details = []

# User Details
user = {
    "fname": '',
    'lname': '',
    'email': ''
}

letter = string.ascii_lowercase
print('Hello there! To get started, we will need your Details...')

# Accepting details from user
while True:
    user['fname'] = input('Enter First Name: ')
    user['lname'] = input('Enter Last Name: ')
    user['email'] = input('Enter Email: ')

    # defining variables to generate a random password
    first_name_first_letters = user['fname'][0:2]
    last_name_first_letters = user['lname'][0:2]
    name_password_part = first_name_first_letters + last_name_first_letters
    user['password'] = name_password_part+ '' .join(random.choice(letter) for i in range(6))
    print(f"This is your password: {user['password']}")


    # Changing user password
    change_password = input('Do you want this as your password? YES | NO: ').upper()
    if change_password == 'NO':
        user['password'] = input('Enter Your Desired Password(password is at least 7 characters): ')
        while len(user['password']) < 7:
            user['password'] = input('Please Enter a password with at least 7 characters: ')

    # Append Details to Users list
    users_details.append(user)
    print('Here are your Details')
    print(f'''
Full Name: {user['fname']} {user['lname']}
Email: {user['email']}
Password: {user['password']}
''')

    # Adding New User
    add_newUser = input('Add another User? Y/N:').upper()
    if add_newUser == 'Y':
        print('Enter details of user2')

    else:
        for user in users_details:
            print(user)
        break
