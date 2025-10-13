s = "joao victor lima da silva"
s_unique = ""

for char in s:
    if char not in s_unique and char != ' ':
        s_unique += char
print(f"there is {len(s_unique)} unique letters in '{s}'")
print("they are:")
for char in s_unique:
    print(char, end = ' ')
print()