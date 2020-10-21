def fun1(num1, num2):
    print(num1)
    if num1 < num2:
      fun1(num1+1, num2)
  
fun1(1,9)
print("____________________________")

def fun2(num3, num4):
    if num3 < num4:
        #print(num3)
        fun2(num3+1, num4)
    print(num3)
    
fun2(1,9)