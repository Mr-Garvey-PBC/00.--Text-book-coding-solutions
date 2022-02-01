password='textbook'
name=str(input('Please enter your name: '))
while name!='Maureen':
    name=str(input('Invalid entry. Please try again: '))
else:
    print('Success, welcome Maureen')
    user_in=str(input('Please enter you password Maureen: '))
    while user_in!=password:
        user_in=str(input('Invalid password. Please try again: '))
    else:
        print('Password entry successfull')