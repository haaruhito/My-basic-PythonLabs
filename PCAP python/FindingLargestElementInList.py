myList = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = myList[0] #Assuming the first element is the largest.

for i in myList[1:]: # comparision is done from second element to end. 
    if i > largest:
        largest = i

print(largest)