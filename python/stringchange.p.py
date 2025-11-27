string=input("Enther the sentance: ").split(' ')

string1=string[0]
string2=string[-1]

first=string2[0]+string1[1:]
last=string1[0]+string2[1:]
center=' '.join(string[1:-1])

word=first+" "+center+" "+last
print(word)
