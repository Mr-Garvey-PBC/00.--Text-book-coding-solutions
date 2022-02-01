user_in=0
total=0
count=1
while user_in>=0:
    user_in=int(input(f'Please enter number {count}: '))
    if user_in>0:
        total=total+user_in
    count+=1

print(f'The average of all your {count} numbers is {total}')