hours = [12, 7, 9, 9, 6, 8, 2] # Hard coded in these hour values but you can use a loop and the apend operation to a manually add the hours
milk_drank=[]  # Creating a blank list to store the amount of milk drank

for i in hours:  # Using a for loop to iterate through the loop elements
    #print(i)    # What would expect to see output to the screen if you uncomment this print statement
    milk_drank.append(i*0.5) # Multiply each element of the hours list by 0.5 and append that value to the milk_drank list.

print(sum(milk_drank)) # Using sum to get the sum of all elements in the list, could also use a loop to do the same thing.
print(f'Stephen must pay {round(sum(milk_drank)*1.35,2)}') 