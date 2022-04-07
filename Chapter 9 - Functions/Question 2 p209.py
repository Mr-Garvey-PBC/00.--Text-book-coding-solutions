# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34   <--- Sequence for testing

def fibonacci_recursion(n):
    if n == 1 or n == 2:
        return (1)
    else:
        return (fibonacci_recursion(n-1) + fibonacci_recursion(n-2))
       # Fn = Fn-1 + Fn-2, where n > 1 , this is th formula for caluclating a value
            
print(fibonacci_recursion(10))


# if condition is the base cases
# else is the recursive case