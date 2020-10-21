def fun1(num):
    if num == 0:
        print(0)
    else:
        fun1(num -1)
        print (num)

fun1(5)