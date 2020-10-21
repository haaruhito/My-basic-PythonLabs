userWord = str(input("Enter a word: "))
userWord = userWord.upper() 
vowels = ("A", "E", "I", "O", "U")

for letter in userWord:
    
    if letter in vowels: 
        continue
        
    else:
        print(letter)
   
        

