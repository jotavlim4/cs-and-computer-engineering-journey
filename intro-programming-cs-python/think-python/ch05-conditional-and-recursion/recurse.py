def recurse(n, s):
	""" n: inteiro positivo ou nulo
		s: valor qualquer
		retorna a soma de s com os a soma dos n primerios
		números inteiros positivos 
	"""
	if n == 0:
		print(s)
	else:
		recurse(n - 1, n + s)

if __name__ == '__main__':
	# recurse(-1, 0) gera recursão infinita.
	recurse(5, 10)
