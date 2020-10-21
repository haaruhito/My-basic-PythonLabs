myList = ["A", "B", 1, 2]

print("A" in myList) # outputs: True
print(2 not in myList) # outputs: False


newList = myList[:] #this copies all elements of myList in newList

print (newList)

anotherList = myList[0:2] #copies part of the list

print (anotherList)