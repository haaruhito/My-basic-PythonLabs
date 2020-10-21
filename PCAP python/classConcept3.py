class Computer:

    def __init__(self, processor, ram):  #Lets pass the same parameters created in the object into this init method. 
                                        #self is the object, processor and ram are other parameters of objects.
        self.processor = processor      #processor, and ram are attributes here. So, they take values when objects are
                                        #created and parameters of these attributes are passed. 
        self.ram = ram


    def config(self):
        print(self.processor, self.ram)

comp1 = Computer('i5', 16) # Lets pass two parameters i5 as processor and 16gb as RAM which goes to init method. 
comp2 = Computer('i3', 8) #

comp1.config() #first object is called
comp2.config() #second object is called