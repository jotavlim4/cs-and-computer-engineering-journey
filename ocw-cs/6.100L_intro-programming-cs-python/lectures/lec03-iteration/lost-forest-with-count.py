where = input("go left or right: ")
count = 0

while where != "left":
    count += 1
    if count > 2:
        print(":(")
    where = input("go left or right: ")
print("you got out!")
