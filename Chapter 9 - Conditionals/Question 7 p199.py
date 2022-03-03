def compare_strings(string1,string2):
    if sorted(string1)==sorted(string2):
        print('These strings are identical')
    else:
        print('They are not identical')

value1=str(input('Enter string 1: '))
value2=str(input('Enter string 2: '))
compare_strings(value1,value2)


