username = input('Enter username: ')
email = input('Enter email: ')
pwd = input('Enter password: ')
cpwd = input('Confirm password: ')

if len(username) > 0 and username.isalnum():
    if len(email) > 0 and '@' in email:
        if len(pwd) >=4:
            if pwd == cpwd:
                print('Registration successful')
            else:
                print('Passwords do not match')
        else:
            print('Password must be at least 4 characters')
    else:
        print('Invalid email')
else:
    print('Username is invalid')