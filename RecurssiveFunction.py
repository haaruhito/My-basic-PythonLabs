# Recursive implementation of the factorial function
def factorial(n):
    if n == 1:    # the base case (termination condition), process terminates in this condition
        return 1
    else:
        return n * factorial(n - 1) #it works like loop

print(factorial(4)) # 4 * 3 * 2 * 1 = 24

