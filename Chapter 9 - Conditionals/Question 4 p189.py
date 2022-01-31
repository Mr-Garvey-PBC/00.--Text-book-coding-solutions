moped_type=str(input('Please enter moped size, 50 or 250: '))
rental_length=float(input('Enter how long you want to rent the moped for in hours: '))
day_rent=str(input('Do you want to rent on a Week(end) or Week(day): '))
price=0


if moped_type=='50' and day_rent == 'day':
    if rental_length > 3:
        price = (15*3)+(2.5*(rental_length-3))
        print(f'The price of your rental is {price}')
    elif rental_length < 3:
        price = (15*rental_length)
        print(f'The price of your rental is {price}')

if moped_type=='50' and day_rent == 'end':
    if rental_length > 3:
        price = (30*3)+(3*(rental_length-3))
        print(f'The price of your rental is {price}')
    elif rental_length < 3:
        price = (30*rental_length)
        print(f'The price of your rental is {price}')
        
if moped_type=='250' and day_rent == 'day':
    if rental_length > 3:
        price = (25*3)+(3.5*(rental_length-3))
        print(f'The price of your rental is {price}')
    elif rental_length < 3:
        price = (25*rental_length)
        print(f'The price of your rental is {price}')

if moped_type=='250' and day_rent == 'end':
    if rental_length > 3:
        price = (35*3)+(5*(rental_length-3))
        print(f'The price of your rental is {price}')
    elif rental_length < 3:
        price = (35*rental_length)
        print(f'The price of your rental is {price}')