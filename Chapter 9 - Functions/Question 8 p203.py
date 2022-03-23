def pet(pet_type,food_eaten):
    if pet_type=='cat':
        return (3*(5*food_eaten))
    else:
        return (3*(3*food_eaten))
    
user_pet=input('What type of pet do you have (hamster or cat): ')
user_pet=user_pet.lower()
quantity_eaten=float(input('How much food do they eat in a week kg: '))
returned_cost=pet(user_pet,quantity_eaten)
print(f'The cost of food for 3 weeks is {returned_cost}')
