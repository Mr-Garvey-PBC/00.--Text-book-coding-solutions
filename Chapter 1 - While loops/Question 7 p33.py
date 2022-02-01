print('Welcome to Lucys Shop\n')
user_in=int(input('Please make a selection\n1. Curtains section\n2. Cushion section\n3. Quilts section\n4. Exit\nEnter Department: '))
while user_in!=4:
    if user_in==1:
        print('\nWelcome to the curtain section')
    elif user_in==2:
        print('\nWelcome to the cushion section')
    elif user_in==3:
        print('\nWelcome to the quilts section')
    else:
        print('\nInvalid option')
    user_in=int(input('\nPlease make a selection\n1. Curtains section\n2. Cushion section\n3. Quilts section\n4. Exit\nEnter Department:'))
print('Thanks for visiting')