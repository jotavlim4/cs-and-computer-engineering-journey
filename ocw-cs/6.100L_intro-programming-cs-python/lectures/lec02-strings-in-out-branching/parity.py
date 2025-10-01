x = 10
# se o resto da divisão de x por 2 é igual a zero
# significa que x é multiplo de 2 e portanto é par.
if x % 2 == 0:
    print("even")
# caso contrário é impar, pois deixa resto 1.
# lembrando que o intervalo de valores possíves para operação x % y
# [0, y-1].
else:
    print("odd")
    
# apenas um dos códigos é executados.