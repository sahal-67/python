numbers=input("enter the numbers: ")
num= list(map(int, numbers.split()))
array=[]

for i in num:
    if(i>100):
     array.append("over")
    else:
        array.append(i)

print(array)
