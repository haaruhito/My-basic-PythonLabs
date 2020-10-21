class User:
    pass        #pass means it does nothing. I am using this just for an example. 


user1 = User()  # object is created, that is user1
user1.first_name = "Dave"   # I am attaching data to the object, user1
user1.last_name = "Sapkota"
user1.age = 37

print(user1.first_name, user1.last_name)

help(User) #It gives an overview how class User can be used.
