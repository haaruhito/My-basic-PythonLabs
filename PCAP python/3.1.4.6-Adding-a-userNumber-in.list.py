hatList = [1, 2, 3, 4, 5]
userNumber = int(input("Enter a number: "))
hatList[2] = userNumber
del hatList[4]
print(len(hatList))
print(hatList)
