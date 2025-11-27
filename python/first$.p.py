word=input("Enter a word : ")
first=word[0]

string=first + word[1:].replace(first,'&')

print(string)
