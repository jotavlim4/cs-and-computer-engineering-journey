import random
secret = int(random.random() * 100)
found = False
for guess in range(1, 11):
    if guess == secret:
        found = True
        break

if not found:
    print("the secret is not that range")
