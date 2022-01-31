import re  # This imports the regular expression module in Python,
           # This module is very powerful and allows you easily analyse data for specific data.
           # See more here https://docs.python.org/3/howto/regex.html
           # https://www.w3schools.com/python/python_regex.asp

print('Conditions for a valid email are\n1.Minimum of 8 characters\n2.At least one .\n3.An @ symbol before the .')
email=str(input('\nPlease enter your email address: '))

search_conditions = '^[a-zA-Z0-9]+[@][.]?'

if(re.search(search_conditions,email)) and len(email)>8:
    print('Valid')
else:
    print('Invalid')
    
# Search conditions explained.
# ^ Tells the program that the following sequence of characters is what decides if an input is valid or not
# [a-zA-Z0-9]+ Tells the search that valid characters allowed are any letter or number
# The + just means that the valid characters will be more than 1 letter or number
# [@] This just means we are looking for the @ symbol, the order of the search matters so the @ must come after a sequence of leters and numbers
# [.] similar to the @ above.