def factorial(n):
	'''
	recebe um número inteiro não negativo
	e retorna o fatorial desse número usando
	chamadas recursivas.
	'''
	if n == 0:  # 0! = 1
		return 1
	else:
		recurse = factorial(n - 1)
		return n * recurse



if __name__ == '__main__':
	x = int(input())
	print(factorial(x))

	