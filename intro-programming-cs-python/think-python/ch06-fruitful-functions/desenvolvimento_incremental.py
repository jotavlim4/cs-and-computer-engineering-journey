import	math

def hypotenuse(a, b):
	'''
	recebe dois valores inteiros que representam
	catetos de um triangulo retangulo e retorna
	o valor da hipotenusa.
	''' 
	return math.sqrt(a**2 + b**2)

def distance(x1, y1, x2, y2):
	'''
	recebe 4 valores correspondedo a coordenadas 
	de dois pontos no plano. retorna a distancia
	entre esses dois pontos.
	'''
	dx = x2 - x1
	dy = y2 - y1
	return hypotenuse(dx, dy)


if __name__ == '__main__':

	x1 = int(input())
	y1 = int(input())
	x2 = int(input())
	y2 = int(input())

	ans = distance(x1, y1, x2, y2)
	print(f"A distância entre os pontos ({x1}, {y1}) e ({x2}, {y2}) é {ans: .2f}")