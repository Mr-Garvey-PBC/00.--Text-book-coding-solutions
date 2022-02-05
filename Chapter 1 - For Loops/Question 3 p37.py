user_in=str(input('Please enter a string: '))
count=0
for i in (user_in):
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        count+=1
print(f'There are {count} vowels in your string')