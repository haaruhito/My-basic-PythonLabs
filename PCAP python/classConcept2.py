class Computer:

    def __init__(self):  #init is a special method, and we are passing self which is an object
        print("in init")

        #Here "in init" will print 3 times because "self" calls both objects comp1, comp2 and comp3
        # For every object, this init method is called once. 

    def config(self):
        print("processor, i5, 16gb RAM, 1tB ROM") #This is printed only once when an object is called. 

comp1 = Computer() #first object created from class
comp2 = Computer() #second object created from class
comp3 = Computer() #third object

comp1.config() #first object is called
comp2.config() #second object is called