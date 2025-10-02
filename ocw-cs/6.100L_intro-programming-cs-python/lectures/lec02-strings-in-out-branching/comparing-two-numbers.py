x = int(input("enter a number for x: "))
y = int(input("enter a different number for y: "))

if x == y:
    print("x and y are equal")
    if y != 0:
        print("therefore, x / y =", x / y)
elif x < y:
    print("x is smaller")
else:
    print("y is smaller")

print("thanks!")
