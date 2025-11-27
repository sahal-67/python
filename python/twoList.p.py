list1=list(map(int, input("Enter multiple integers separated by spaces: ").split())) 
list2=list(map(int, input("Enter multiple integers separated by spaces: ").split()))

if(len(list1)==len(list2)):
    print("the given list are the same length")
else:
       print("the given list are not same length")

if(sum(list1)==sum(list2)):
    print("the list sums are same value")
else:
       print("the list sums not same value")

same=[]
setas=False
for i in list1:
    for j in list2:
        if(i==j):
            same.append(i)
            setas=True

if(setas==False):
    print("there is no same values")
else:
        print(f"the values occure in both={same}")
        
    
            

