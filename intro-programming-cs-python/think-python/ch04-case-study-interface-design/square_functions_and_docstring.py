import math
import turtle

bob = turtle.Turtle()

def square(t, lenght):
	'''
	parametros: t, um objeto tipo Turtle e lenght, um valor positivo que representa o tamanho do quadrado.
	retorno: um quadrado de lado lenght.
	'''
	for i in range(4):
		t.fd(lenght)
		t.lt(90)

def polyline(turtle, lenght, n, angle):
	"""
	recebe como parametros um objeto turtle, o valor positivo lenght que resenta o tamanho da linha desenhada,
	um inteiro positivo n e um angulo.
	retorna n segmentos de tamanho lenght e o angulo angle entre as eles.
	"""
	for i in range(n):
		turtle.fd(lenght)
		turtle.lt(angle)

def polygon(t, lenght, n):
	"""
	recebe um objeto turtle t, um valor positiov para lenght e um inteiro positivo n.
	desenha um poligono de lado lenght.
	"""
	angle = 360/n
	polyline(t, lenght, n, angle)

def arc(turtle, radius, angle):
	"""
		recebe um objeto turtle, um valor positivo para o raio do circulo e um valor positivo para o angulo.
		retorna um arco de uma circufenrecia de raio dado e angulo angle.
	"""
	arc_lenght =  2 * math.pi * radius * (angle / 360)
	n = int(arc_lenght / 3) + 1
	step_lenght = arc_lenght / n
	step_angle = float(angle) / n
	polyline(turtle, step_lenght, n, step_angle)


def circle(turtle, radius):
	"""
		recebe um objeto turtle e o valor positivo para o raio.
		retorna um ciruclo de raio dado.
	"""
	arc(turtle, radius, angle = 360)

circle(bob, 100)

turtle.mainloop()
