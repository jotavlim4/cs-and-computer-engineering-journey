"""Write a program that examines three variables—
x, y, and z—and prints the largest odd number among them. If none
of them are odd, it should print the smallest value of the three. """

x = 70
y = 10
z = 20

# só imprimimos o valor mínimo quando não há impares entre os números testados
# então inicializamos a resposta com o menor entre eles
answer = min(x, y, z) 

# se existir um número impar, então ele será nossa resposta atual.
# verificamos se existe outro impar, caso exista comparamos com o atual
# e atualizamos a resposta se for necessário.

if x % 2 != 0:
    answer = x
if y % 2 != 0 and y > answer:
    answer = y
if z % 2 != 0 and z > answer:
    answer = z

print(answer)

