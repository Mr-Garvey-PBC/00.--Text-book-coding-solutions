user_in=str(input('Please enter a string of any length: '))
index_position=0
count=0
while index_position<len(user_in):
    if user_in[index_position]==' ':
        count+=1
    index_position+=1
print(count)

# Or a simpler solution not using a while loop
#print(user_in.count(' '))