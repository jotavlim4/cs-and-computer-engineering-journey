def countdown(n):
	if n <= 0:
		print('Blastooff!')
	else:
		print(n)
		countdown(n-1)

countdown(7)