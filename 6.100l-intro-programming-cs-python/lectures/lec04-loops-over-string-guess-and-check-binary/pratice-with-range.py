# print(*range(5)) # 0 1 2 3 4
# print(*range(10)) # 0 1 2 3 4 5 6 7 8 9
# print(*range(2, 9, 3)) # 2 5 8
# print(*range(-4, 6, 2)) # -4 -2 0 2 4
# print(*range(5, 6)) # 5

total = 0
for i in range(5):
    if i % 2 == 0:
        total += 1
print(total)

total = 0
for i in range(10):
    if i % 2 == 0:
        total += 1
print(total)

total = 0
for i in range(2, 9, 3):
    if i % 2 == 0:
        total += 1
print(total)

total = 0
for i in range(-4, 6, 2):
    if i % 2 == 0:
        total += 1
print(total)

total = 0
for i in range(5, 6):
    if i % 2 == 0:
        total += 1
print(total)