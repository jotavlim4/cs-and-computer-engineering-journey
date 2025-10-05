'''
Escreva uma função 'circle_area' que calcula a área de um circulo
dadas as coordenadas do centro do círculo e as 
coordenadas de um ponto que está no perimetro do círculo.

Use as funções 'distance' e 'area' para cálcular.
'''

import math


def hypotenuse(a, b):
	'''
	recebe dois valores correspondentes aos catetos de um
	triangulo retangulo e retorna o valor da hipotenusa.
	'''
	return math.sqrt(a**2 + b**2)

def distance(x1, y1, x2, y2):
	'''
	recebe coordenadas de dois pontos no plano
	e calcula a distance entre eles
	'''
	dx = x2 - x1
	dy = y2 - y1
	return hypotenuse(dx, dy)

def area(r):
	'''
	recebe o raio de uma circunferência 
	e desolve o area do circulo de tal raio.
	'''
	return math.pi*(r**2)

def circle_area(xc, yc, xp, yp):
	'''
	recebe como entrada as coordendas do centro do circulo
	e as coordenadas de um ponto do perimetro.
	retorna o área de tal circulo.
	'''
	radius = distance(xc, yc, xp, yp)
	return area(radius)
	
if __name__ == '__main__':
	x1 = int(input())
	y1 = int(input())
	x2 = int(input())
	y2 = int(input())

	ans = circle_area(x1, y1, x2, y2)
	print(f"A área do círculo de centro ({x1}, {y1}) cujo o seguinte ponto ({x2}, {y2}) pertence a seu perimetro é {ans:.2f}")