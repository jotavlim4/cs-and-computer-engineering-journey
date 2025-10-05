def is_between(x, y, z):
	'''
	Recebe três números como argumentos e
	verifica se o segundo número está entre 
	os outros dois. Retorna True se estiver,
	False caso contrário.
	'''
	if x <= y <= z: 
		return True
	else: 
		return False


if __name__ == '__main__':
	x = int(input())
	y = int(input())
	z = int(input())

	ans = is_between(x, y, z)
	print(ans)