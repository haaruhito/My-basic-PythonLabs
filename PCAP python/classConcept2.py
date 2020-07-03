class computer:

    def __init__(self):  #init is a special method, and we are passing self which is an object
        print("in init")

    def config(self):
        print("processor, i5, 16gb RAM, 1tB ROM")

comp1 = computer() #first object created from class
comp2 = computer() #second object created from class

comp1.config() #first object is called
comp2.config() #second object is called