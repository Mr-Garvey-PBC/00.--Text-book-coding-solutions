# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34   <--- Sequence for testing

def fibonacci(n):
    secondLast = 0   # First value in the sequence
    Last = 1         # Second value in the sequence
    
    if n == 1:       # If you are looking for the first value (n=1) in the sequence it is always 0
        print(secondLast)
    elif n == 2:
        print(Last)  # If you are looking for the second value (n=2) in the sequence it is always 0
    else:
        for i in range (3, n+1):  # Using iteration to start at the thd term and go to n+1 a for loop will always stop bfore the end range value
            result = secondLast + Last  # Fn = Fn-1 + Fn-2, where n > 1 , this is th formula for caluclating a value
            secondLast = Last
            Last = result
        print(result)

fibonacci(5) # Call to function

# if and elif conditions are the base cases
# else is the recursive case