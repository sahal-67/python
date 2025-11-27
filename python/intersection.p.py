list1=input("Enter the colours of list one: ").split(' ')
list2= input("Enter the colors of list two: ").split(' ')


for color in list1:
    if color not in list2:
        print(color)
