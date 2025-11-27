num1, num2, num3 = map(int, input("Enter three numbers separated by spaces: ").split())
biggest = max(num1, num2, num3)
print(f"The biggest number is: {biggest}")

#many number
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
biggest = max(numbers)
print(f"The biggest number is: {biggest}")
