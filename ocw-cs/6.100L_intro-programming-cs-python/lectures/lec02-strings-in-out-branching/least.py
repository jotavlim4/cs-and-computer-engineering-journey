x = 10
y = 5
z = 30


if x < y and x < z:       # se esse condição não for verdadeira, nao precisamos
    print("x is least")   # não precisamos comparar o próximo número com x, pois já comparados
elif y < z:               # y já foi comparado com x, logo, só resta compará-lo com z
    print("y is least")   # caso aconteça de y < z ser falso, esgotamos todas as possbilidaes
else:                     # e só resta z para ser o menor dos valores.
    print("z is least")