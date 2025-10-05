import turtle
import math

bob = turtle.Turtle()

bob.pu()
bob.bk(500)
bob.pd()
bob.speed(1)



def draw_pie(t, lenght, n):
	"""
	recebe como parametros um objeto turtle, o valor positivo para o tamanho
	do raio do poligono inscrito e a quantidade de triangulos isosceles que serão
	desenhados. desenha os poligonos e em seguida avança para a direita sem deixar
	rastro para que outro poligono possa ser desenhado.	
	"""
	polypie(t, lenght, n)
	t.pu()
	t.fd(lenght*2 + 10)
	t.pd()


def polypie(t, lenght, n):
	"""
	recebe como parametros um objeto turtle, o valor positivo para o tamanho
	do raio do poligono inscrito e a quantidade de triangulos isosceles que serão
	desenhados.
	"""
	angle = 360.0 / n 
	for i in range(n):
		triangle(t, lenght, angle/2)
		t.lt(angle)


def triangle(t, lenght, angle):
	"""
	recebe como parametros um objeto turtle, o valor positivo para o tamanho
	do raio do poligono inscrito e o angulo central do poligono.
	retorna um triangulo isosceles.
	"""
	y = lenght * math.sin(angle * (math.pi / 180))

	t.lt(angle)
	t.fd(lenght)
	t.rt(90 + angle)
	t.fd(2*y)
	t.rt(90 + angle)
	t.fd(lenght)
	t.rt(180-angle)


triangle(bob, 400, 360/10)

# size = 60
# draw_pie(bob, size, 5)
# draw_pie(bob, size, 6)
# draw_pie(bob, size, 7)
# draw_pie(bob, size, 8)
# draw_pie(bob, size, 9)
# draw_pie(bob, size, 10)
# draw_pie(bob, size, 11)
# draw_pie(bob, size, 12)
# draw_pie(bob, size, 13)
# draw_pie(bob, size, 14)

turtle.mainloop()