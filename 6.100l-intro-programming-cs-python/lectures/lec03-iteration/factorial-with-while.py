number = int(input("type a nonnegative integer: "))
factorial = 1
i = 1;
while i <= number:
    factorial *= i
    i += 1
print(f"{number}! = {factorial}")