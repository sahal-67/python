user=input("enter the sentence : ")
vowels=["a","e","i","o","u","A","E","I","O","U"]

print("the vowels are:  ")
for i in user:
    for j in vowels:
        if(i==j):
            print(i)


