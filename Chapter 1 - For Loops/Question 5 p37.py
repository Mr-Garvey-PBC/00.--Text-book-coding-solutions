user_in=str(input('Please enter a string: '))
key_value=str(input('What would you like to search for (1 character only): '))
count=0
for i in (user_in):
    if i==key_value:
        count+=1
print(f'There are {count} occurences of {key_value} in your string')
