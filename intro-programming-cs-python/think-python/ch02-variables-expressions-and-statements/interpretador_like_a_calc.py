#volume de uma esfera de raio 5
r = 5
volume = (4/3)*3.14*r**3
print("volume da esfera de raio 5", volume)

#preço de um livro
preco_de_capa = 24.95
desconto = 0.4 * preco_de_capa
transporte = 3.0 + 0.75*59
preco_final = (preco_de_capa - desconto)*60 + transporte
print("preço final do pedido de 60 livros:", preco_final) 

#corrida:

#saida de casa: 6h52min
tempo_saida = 6*3600 + 52*60
tempo1 = 8*60 + 15
tempo2 = 3*(7*60 + 12)
tempo_total = tempo_saida + 2*tempo1 + tempo2
print("horário de chegada:", tempo_total//3600, "h", (tempo_total%3600//60), 'min')