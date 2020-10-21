beatles = []
print ("Step 1:", beatles)
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print ("Step 2:", beatles)

userInput = input("Write Stu Sutcliffe or Pete Best to add to list: ")
for i in userInput:
    if i=="Stu Sutcliffe": 
    
        beatles.append(i)
    
    elif i == "Pete Best":   
        beatles.append(i)
    
print(beatles)

#del beatles[]
#del beatles[]
#beatles.insert(0, Ringo Starr)
