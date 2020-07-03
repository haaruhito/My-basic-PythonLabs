
# We can put two things in a class. The first
#thing is attributes (characters or lets 
# say variables) and the second 
# thing is Behavior (methods)

class computer:
     def config(self): # a method is created here and 'self' is the object we are passing. Object is comp1 which is created below.
         print("i5 processor, 16gb RAM, 1TB ROM")


comp1 = computer() #comp1 is an object from class computer.
comp2 = computer() #comp2 is another object

computer.config(comp1)  #computer is class and config is method inside class and comp1 is object created from that class

computer.config(comp2) #prints the same things as comp1

# or we also can call object comp1 and comp2 as follows

comp1.config()
comp2.config()