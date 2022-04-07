def sum_list(list_of_val):
    
    #Base Case
    if len(list_of_val)==1:
        return(list_of_val[0])
    
    else:
        #print(list_of_val)
        #print(f'{list_of_val[0]} + {sum_list(list_of_val[1:])}')
        return(list_of_val[0] + sum_list(list_of_val[1:]))

print(sum_list([6,7,8,9,10]))
