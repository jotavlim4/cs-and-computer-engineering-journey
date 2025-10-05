def fibonacci(n):
	'''
	recebe um inteiro não nulo n e retorna
	o enésimo número da sequencia de fibonacci
	calculado recursivamente.
	'''
	if n == 0:
		return 1
	elif n == 1:
		return 1
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':
	print(fibonacci(20))