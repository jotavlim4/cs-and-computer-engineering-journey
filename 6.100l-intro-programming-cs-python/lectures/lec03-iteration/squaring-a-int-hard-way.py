x = 3
ans = 0
num_interarions = 0
while num_interarions < x:
    ans = ans + x
    num_interarions = num_interarions + 1
    
print(f"{x}*{x} = {ans}")

# observe que o loop while é finalizado para as seguintes situações:

# (1) x == 0. nesse caso 'num_interarions < x' é avaliado como falso e 
# o programa segue para a instrução print.

# (2) x < 0. 0 < numero negativo é falso, logo o código não é executado e o controle
# vai diretamente para a função print

# (3) x > 0. o loop é executado no mínimo uma vez e a condição de Falso é atigida em algum
# momento pois  'num_interarions = num_interarions + 1' garante isso.