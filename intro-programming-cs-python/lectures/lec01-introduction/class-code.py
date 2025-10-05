# verificando tipos de dados
print("verificando tipos de dados:")
print(type(1234)) # int
print(type(8.99)) # flaot
print(type(9.0)) # float
print(type(True)) # bool 
print(type(False)) # bool
print()

# verificando tipo de dados após o casting
print("verificando tipo de dados após o casting:")
print(type(float(123))) # float 
print(type(round(7.9))) # int
print(type(float(round(7.2)))) # float
print(type(int(7.2))) # int 
print(type(int(7.9))) # int 
print()

# verificando os valores após a conversão explícita
print("verificando os valores após a conversão explícita:")
print(float(123)) # float  -> 123.0
print(round(7.9)) # int -> 8
print(float(round(7.2))) # float -> 7.0
print(int(7.2)) # int -> 7
print(int(7.9)) # int -> 7
print()

# entendendo o comportamento de round
print("entendendo o comportamento de round:")
print(round(1.0))
print(round(1.1))
print(round(1.2))
print(round(1.3))
print(round(1.4))
print(round(1.5))
print(round(1.6))
print(round(1.7))
print(round(1.8))
print(round(1.9))
print()

# avaliando expressoões
print("avaliando expressoões:")
print((13-4) / (12*12)) # 0.625
x = type(4*3)
print(x) # int
x = type(4.0*3)
print(x) # float
print(int(1/2)) # 0
print()

# operação de atribuição e nome de variáveis
x = 6 # valido 
6 = x # inválido
x*y = 3+4 # inválido
xy = 3+4 # válido

# entendendo reatibuição
meters = 100
feet = 3.2808 * meters
meters = 200 # apesar de reatribuído, o valor de feet é o produzido pelo antigo valor de meters

print(feet)

# trocando valores

x = 2
y = 3

# por que não funcion? 
x = y
y = x

print(x) # 3
print(y) # 3

# não funciona, pois ao realizar x = y, o valor anterior de x, 2, é perdido.
# x fará apeneas referencia ao valor 3.
# quando fazemos y = x, estamos na verdade, avaliando x com 3, e dando y como nome
# ao valor 3.

