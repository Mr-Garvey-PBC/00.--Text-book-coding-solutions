def temp_converter(temp_value,scale_used):
    if scale_used=='c':
        fah_val=(temp_value*1.8)+32
        return fah_val
    elif scale_used=='f':
        cel_val=(temp_value-32)*0.5666
        return cel_val
    
scale_select=input("Please select temp scale you are using 'c' for Celsius or 'f' for Fahrenheit: ")
scale_select=scale_select.lower()
temp_input=float(input('Please enter temperature to convert: '))
print(f'Your converted temperature is {temp_converter(temp_input,scale_select)}')
