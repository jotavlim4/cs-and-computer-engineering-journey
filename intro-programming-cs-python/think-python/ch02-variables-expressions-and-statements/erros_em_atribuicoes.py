#testando a ordem da operação de atribuição:

n = 2 #legal
#2 = n ilegal -> SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?

x = y = 1 #legal -> estamos atribuido 1 a y e depois o valor que está em y a x, nesse caso o próprio 1

#testando terminar instruções com ';':
print("testando terminar instruções com ';'"); #legal

#testando terminar instruções com '.':
#print("testando terminar instruções com '.'"). -> SyntaxError: invalid syntax

#testando realizar a operação de multiplicação sem usar *:
print(35) #é necessário usar o operador da multiplicação para que o produto ocorra.
print(3*5)

