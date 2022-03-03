ppm=float(input('What is the price per square meter: '))

width=[5,10,15,20]
length=[10,20,30,40,50,60,70,80,90,100]
list_index=0

for i in length:
    for j in width:
        print(round(i*j*ppm),end='  ')  
    print()