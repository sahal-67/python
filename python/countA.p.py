names=input("enter the full names with commas: ")
nam=names.split(",")
first=[]

for i in nam:
    first.append(i.split()[0])

print(f"the first names {first}")    

count=0
for i in first:
    count+=i.count('a')
print(f"'a' in the first names= {count}")

