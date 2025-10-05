number = int(input("enter a nonnegative integer: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"{number}! = {factorial}")