#f(y) = f(x-1) + f(x-2)

def f1(x):
    return(x-1)
def f2(x1):
    return(x1-2)
def f_y(f1,f2):
    return (f1+f2)
#print(f1(3))
#print(f2(10))
print(f_y(f1(10), f2(21)))

print("...................................")

for i in [f1,f2]:
    print(i(2))

print(type(f1))