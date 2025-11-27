numbers=input("enter the numbes: ")
positive=[]

num = list(map(int, numbers.split()))
print(num)
setas=False

for i in num:
    if(i>0):
        positive.append(i)
        setas=True

if(setas==False):
    print("there is no positive number")
else:
        print(f"the positive numbers are: {positive}")
