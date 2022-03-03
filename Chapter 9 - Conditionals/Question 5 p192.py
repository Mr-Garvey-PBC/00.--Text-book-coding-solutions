rows=int(input('How many rows would you like: '))
print('\n')
    
for i in range(1,rows+1):
    print(("*"*i).rjust(rows))

# Link to website where i found solution, you can do it with f-strings as well.
# https://www.kite.com/python/answers/how-to-right-align-a-number-in-python#:~:text=Use%20the%20syntax%20f%22%7Bnumber,to%20a%20length%20of%20width%20.&text=Further%20reading%3A%20Python's%20f%2Dstring,powerful%20way%20to%20format%20strings.