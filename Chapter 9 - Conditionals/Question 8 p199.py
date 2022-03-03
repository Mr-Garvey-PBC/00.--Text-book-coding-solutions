import re  # This imports the regular expression module in Python,
           # This module is very powerful and allows you easily analyse data for specific data.
           # See more here https://docs.python.org/3/howto/regex.html
           # https://www.w3schools.com/python/python_regex.asp

def confirm_email(email):
    search_conditions = '^[a-zA-Z0-9]+[@][.]?'

    if(re.search(search_conditions,email)) and len(email)>8:
        print('Valid')
    else:
        print('Invalid')

print('Conditions for a valid email are\n1.Minimum of 8 characters\n2.At least one .\n3.An @ symbol before the .')
email=str(input('\nPlease enter your email address: '))
confirm_email(email)