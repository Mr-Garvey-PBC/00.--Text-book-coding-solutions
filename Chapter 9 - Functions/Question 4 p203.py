def check_for_even_divide(num1,num2):
    if num1%num2==0:
        return True
    else:
        return False

if check_for_even_divide(5,3)==True:
    print('Your numbers divide evenly')
else:
    print('Your numbers dont divide evenly')
