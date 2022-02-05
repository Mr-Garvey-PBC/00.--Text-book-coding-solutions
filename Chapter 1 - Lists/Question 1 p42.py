list_of_numbers=[] # Declare blank list

for i in range(5):
    user_in=int(input('What number do you want to add to the list: '))
    list_of_numbers.append(user_in)   # Using the append operation to add the user_in value to the list.

for i in range(len(list_of_numbers)): # Use a for loop to iterate through the list
    list_of_numbers[i] = list_of_numbers[i]+1 # Use the i value as an index position identifier for elements of the list and add 1 to them

print(list_of_numbers)