side_1=int(input('Please enter the first length of your triangle: '))
side_2=int(input('Please enter the second length of your triangle: '))
side_3=int(input('Please enter the final length of your triangle: '))

#The hypotenuse is always the longest side in a right triangle
hyp=side_1
opp=side_2
adj=side_3

if (side_2>side_1) and (side_2>side_3):
    hyp=side_2
    opp=side_1
    adj=side_3
elif (side_3>side_1) and (side_3>side_2):
    hyp=side_3
    opp=side_1
    adj=side_2

if hyp**2==(opp**2)+(adj**2):
    print('Triangle is right angle')
else:
    print('Triangle not a right angle')