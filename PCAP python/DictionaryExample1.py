#English-French dictionary
print("1. An example to check if key exist in dictionary.")

dictionary = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"} #it is a dictionary
words = ['cat', 'lion', 'horse'] #It is list

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")


#Another example
print("\n2. Another example...it prints value when we give its key")
print(dictionary['cat'])
print(dictionary['dog'])
print(dictionary['horse'])


#Another example that prints all keys:values of dictionary
print("\n3. Another example...It prints all key-value pairs using for loop")
for key in dictionary.keys():
    print(key, "->", dictionary[key])


print("\n4. Another example...It also returns key and value pairs using dictionary.items")
for english, french in dictionary.items():
    print(english, "->", french)


print("\n5. Another example which prints only values using dictionary.values")
for french in dictionary.values():
    print(french)

#Adding a new key-value pair in a dictionary
print("\n6. Adding a new key-value pair to a dictionary.\n")
dictionary['swan'] = 'cygne'
print(dictionary)


#We can also insert an item to a dictionary by using a method

print("\n7. We can also insert an item to a dictionary by using a method.\n")

dictionary.update({"duck" : "canard"})
print(dictionary)

#Deleting a key from dictionary
print("\n7. We can delete a key using del. \n")
del dictionary['dog']
print(dictionary)