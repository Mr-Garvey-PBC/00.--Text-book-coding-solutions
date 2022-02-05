rain_per_day=[] # Declare blank list

for i in range(7):
    user_in=float(input('How much rain fell today: '))
    rain_per_day.append(user_in)

print(f'\nTHe total rain fall this week was {sum(rain_per_day)}')
print(f'The average rain fall was {sum(rain_per_day)/7}')

for i in rain_per_day:
    if i>3.5:
        print('\nRain today was over 3.5mm')
    