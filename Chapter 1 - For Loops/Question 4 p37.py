user_in=str(input('Please enter a string: '))
reversed_string='' # Creating a blank string to add the string values to
for i in (user_in):
    reversed_string=i+reversed_string
print(f'Your in put backwards is {reversed_string}')