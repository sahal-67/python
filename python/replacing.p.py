word=input("Enter a word : ")
first=word[0]
last=word[-1]

string=last + word[1:-1] + first

print(string)
