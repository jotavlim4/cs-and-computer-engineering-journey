cube = int(input("enter an integer: "))
for guess in range(abs(cube) + 1):
    if guess**3 >= abs(cube): # interrompe o loop quando o cubo de 'guess' for maior ou igual que cube. 
        break                 # das duas uma: ou encontramos o cubo perfeito ou ultrapassamos.
if guess**3 != abs(cube): # aqui verificamos o que de fato houve.
    print(f"{cube} is not a perfect cube")
else:
    if cube < 0: # para lidar com a possibilidade do valor digitado ser negativo.
        guess = -guess
    print(f"the cube root of {cube} is {guess}")
