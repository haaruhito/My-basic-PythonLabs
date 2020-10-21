myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# put your code here
#

newList = []
for i in myList:
    if i not in newList:
        newList.append(i)
     
print("The list with unique elements only:", newList)
print(myList)