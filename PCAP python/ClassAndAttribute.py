class Dog:
    def __init__(self, name, age): #name and age are attributes.
        self.name = name
        self.age = age
        
    def get_name(self): #This is a method under class Dog. 
        return self.name

    def get_age(self):
        return self.age

d1 = Dog("Tommy", 30)
print(d1.name)

print(d1.get_name())

print(d1.get_age())