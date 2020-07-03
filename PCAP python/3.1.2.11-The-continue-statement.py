wordWithoutVowels =""
userWord = input("Enter a word: ")
userWord = userWord.upper()
vowels = ("A", "E", "I", "O", "U")

for letter in userWord:
    if letter in vowels:
        continue
    else:
        wordWithoutVowels+=letter
print(wordWithoutVowels)