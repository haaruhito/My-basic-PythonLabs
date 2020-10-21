list1 = [1]
list2 = list1
list1[0] = 2
print(list2)
print(list1)
print("""In the above example, list1 and list2 shares the same memory.
Change in list1 will make differences in list2 and vice-versa.""" )
print("\nBelow is the change")

#Comparision from up and down
list3 = [1]
list4 = list3[:] #list4 is a new list and just copies elements of list3 and they share different memory location.
list3[0] = 2
print(list4)
print(list3)