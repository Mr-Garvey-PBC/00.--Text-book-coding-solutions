# This program works but has a small bug, when you use -1 as the escape value from the while loop it subtracts -1 from the sales_total.
# When you understand this program see if you can use the .pop() method to stop this happening and then try using a condition to prevent this happening.

name_salesperson=[]
salepersons_sales=[]

sales_total=0

number_of_salesperson=int(input('How many sales reps do you have: '))

for i in range(number_of_salesperson):
    salesperson_name=str(input('Enter name: '))
    name_salesperson.append(salesperson_name)
    
    sales_info=float(input(f'\nPlease enter sales data for {salesperson_name}, enter -1 to stop entering sales data: '))
    sales_total=sales_total+sales_info
    while sales_info!=-1:
        sales_info=float(input(f'Please enter sales data for {salesperson_name}, enter -1 to stop entering sales data: '))
        sales_total=sales_total+sales_info
        salepersons_sales.append(sales_info)
        
    print(f'\n{salesperson_name} sold {sales_total}')

print(f'\nThe total value of all sales made was {sum(salepersons_sales)}')
print(f'The largest sale made was {max(salepersons_sales)}')
print(f'The smalles sale made was {min(salepersons_sales)}')
print(f'The average sale made was {round(sum(salepersons_sales)/len(salepersons_sales),2)}')