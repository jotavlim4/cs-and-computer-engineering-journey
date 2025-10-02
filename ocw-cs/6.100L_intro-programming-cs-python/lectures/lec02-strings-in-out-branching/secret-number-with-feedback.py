secret = 10
guess = int(input("choose a number: "))

if guess > secret:
    print('wrong. too high.')
elif guess < secret:
    print("wrong. too low")
else:
    print( "nice. your guess is the same as the secret.")