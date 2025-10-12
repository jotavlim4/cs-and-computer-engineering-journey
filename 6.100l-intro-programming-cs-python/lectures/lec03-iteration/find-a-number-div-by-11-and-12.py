x = 1
while True: # uma forma de criar um loop infinito.
    if x % 11 == 0 and x % 12 == 0:
        break # quando essa instrução é executada, O LOOP MAIS INTERNO é encerrado.
    x = x + 1
print(f"{x} is both divisible by 11 and 12.")

