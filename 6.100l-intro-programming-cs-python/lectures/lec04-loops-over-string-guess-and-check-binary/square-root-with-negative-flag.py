guess = 0 # palpite incial
neg_flag = False # assumimos que o valor é positivo.
x = int(input("type a integer: "))
if x < 0:
    neg_flag = True
while guess*guess < x: # continuamos incrementando o palpite enquanto ele for menor que o valor de x
    guess += 1 
if guess*guess == x: # se o quadrado do palpite for igual ao valor de x, significa que x é um quadrado perfeito.
    print(f"the square root of {x} is {guess}")
else: # se não, significa que o quadrado do palpite é maior que x, logo x não tem quadrado perfeito.
    print(f"{x} is not a perfect square")
    if neg_flag: # mas pode ser que o usuário tenha digitado um número negativo, então checamos isso com ele.
        print(f"just checking... did you mean {-x}?")