count=0

def sale_price(RRP_input,discount_input):
    discount_input=discount_input/100 # Turn discount % input to a decimal
    return (RRP_input-(discount_input*RRP_input))

while count!=6:
    RRP=float(input('Please enter the RRP of the product: '))
    discount=float(input('Please enter discount %: '))
    print(f'The sale price is {sale_price(RRP,discount)}')  # Call to the function within the print statement
    count+=1
#