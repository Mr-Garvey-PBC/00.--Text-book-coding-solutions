limit_value=int(input('Please enter a limit value: '))
count=0
odd_total=0
even_total=0

while count<=limit_value:
    if count%2==0:
        even_total=even_total+count
    elif count%2 != 0:
        odd_total=odd_total+count
    count+=1
print(f'The sum of even numbers is {even_total}')
print(f'The sum of odd numbers is {odd_total}')
        