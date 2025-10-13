number = int(input("type a nonnegative integer: "))
binary = ""
decimal = number
while number > 0:
        binary = str(number % 2) + binary
        number //= 2
print(f"({decimal})_10 = ({binary})_2")