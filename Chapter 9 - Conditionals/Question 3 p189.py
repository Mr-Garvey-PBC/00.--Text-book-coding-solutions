print('Enter your birth month in numeric format\n1=January\n2=February\n3=March\n...etc')
birthday_month=int(input('\nEnter your birth month: '))
current_month=int(input('Enter the current month: '))

if current_month<birthday_month:
    print(f'Your birthday is in {birthday_month-current_month} months time')

elif current_month>birthday_month:
    print(f'Your birthday is in {(12-current_month)+birthday_month} months time')

elif current_month==birthday_month:
    print('Your birthday is in 12 months')
