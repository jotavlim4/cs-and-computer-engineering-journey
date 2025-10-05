def compare(x, y):
	if x > y: 
		return 1
	elif x < y:
		return -1
	else:
		return 0

x = compare(1, 2)
print(x)

# note que pelo menos uma das instruções return será executada, 
# pois todas as possibilidades para comparação entre dois números
# são cobertas.