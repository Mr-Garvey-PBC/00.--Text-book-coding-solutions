count=1
total=0
while count<7:
    user_in=int(input(f'Please enter number {count}: '))
    total=total+user_in
    count+=1
print(f'The average of all your 6 numbers is {total/6}')