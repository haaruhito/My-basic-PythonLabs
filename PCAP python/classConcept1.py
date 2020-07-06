
# We can put two things in a class. The first
# thing is attributes (characters or lets 
# say variables) and the second 
# thing is Behavior or function (methods)

class Computer:             #It is recommended to use first letter capital while naming a class. 
     def config(self): # a method is created here and 'self' is the object we are passing. Object is comp1 which is created below.
         print("i5 processor, 16gb RAM, 1TB ROM")

    # self keyword is only used when creating a method.


comp1 = Computer() #comp1 is an object from class computer.
comp2 = Computer() #comp2 is another object

Computer.config(comp1)  #computer is class and config is method inside class and comp1 is object created from that class

Computer.config(comp2) #prints the same things as comp1

# or we also can call object comp1 and comp2 as follows which is mainly used in coding. 

comp1.config()
comp2.config()