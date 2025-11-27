user=input("enter the sentance: ")
sent=user.split()

count={}

for i in sent:
    if i in count:
        count[i] +=1
    else:
        count[i]=1

print(count)
