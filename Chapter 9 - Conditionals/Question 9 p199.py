def compare_strings(string1,string2):
    count=0
    for i in string1:
        if i==string2:
            count+=1
    print(f'The letter {string2} appears {count} times.')

value1=str(input('Enter string: '))
value2=str(input('Enter letter to check: '))
compare_strings(value1,value2)



