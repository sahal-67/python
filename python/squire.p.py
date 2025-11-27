how= int(input("how many numbers you insert: "))
print("Enter the numbers")

numbers=[]

for num in range(how):
        value=int(input(f"number {num + 1 }: "))
        numbers.append(value)

print("the squires")
for i in numbers:
    squire=i*i
    print(f"{i}={squire}")

                       
          
          
          
    
