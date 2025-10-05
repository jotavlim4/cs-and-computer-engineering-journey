def absolute_value(n):
	if n < 0:
		return -n
	if n > 0:
		return n

x = absolute_value(0)
print(x)

# neste caso, nenhuma das instruções 'return' é alcançada
# então absolute_value(0) retorna None, logo temos print(None)