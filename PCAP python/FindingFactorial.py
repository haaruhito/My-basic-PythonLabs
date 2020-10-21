def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    product = 1
    for i in range(2, n + 1): #recursion is used here. Its like loop.
        product *= i
    return product

for n in range(1, 6): # testing
    print(n, factorialFun(n))