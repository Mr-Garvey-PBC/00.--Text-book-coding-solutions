grade_level=input('Please enter whether you are taking (H)igher or (O)rdinary level: ')
result=int(input('Please enter your result: '))

if result>=90 and result<=100:
    if grade_level=='H':
        print('You got a H1')
    else:
        print('You got an O1')

if result>=80 and result<90:
    if grade_level=='H':
        print('You got a H2')
    else:
        print('You got an O2')
        
if result>=70 and result<80:
    if grade_level=='H':
        print('You got a H3')
    else:
        print('You got an O3')
        
# And repeat all the way down to H8/O8