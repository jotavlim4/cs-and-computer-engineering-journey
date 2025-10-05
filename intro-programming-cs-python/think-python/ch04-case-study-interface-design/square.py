import turtle
import math

bob = turtle.Turtle()

# encapsulamento, significa pegar uma parte do código
# que tem determinada funcionalidade e criar uma função
# com ele. desse modo, evitamento a repetição do código
# quando quisermos que esse comportamento seja efetuado
# outra vez
def square(t, lenght):
	for i in range(4):
		t.fd(lenght)
		t.lt(90)


# generalização, acrescentamos parametros para que tal
# funcionalidade possa ser generalizada, isto é, um mesma
# parte do código serve para diferentes contexto dentro
# de uma tarefa específfica.

# a função square() desenha apenas um quadrado. enquanto que
# a função polygon() desenha qualquer polígono inclusive quadrados. 

def polyline(turtle, lenght, n, angle):
	for i in range(n):
		turtle.fd(lenght)
		turtle.lt(angle)


def polygon(t, lenght, n):
	angle = 360/n
	polyline(t, lenght, n, angle)

# def circle(t, r):
#	circunference = 2 * math.pi * r
#	n = int(circunference / 3) + 1
#	lenght = circunference / n
#	polygon(t, lenght, n)

# a função arc representa uma refatoração da funcao circle, 
# pois agora melhoramos a interface de modo que podemos criar
# tanto um circulo, quando angle = 360, quanto qualquer outra
# arc da circunferencia, quando 0 < angle < 360

# a interface de um função é basicamente um resumo do que ela faz
# então entram no conceito de interface tanto o nome como os parametros.

# uma função com uma interface limpar permite que o usuário faça o que quer
# sem precisar saber COMO a função funciona.

def arc(turtle, radius, angle):
	arc_lenght =  2 * math.pi * radius * (angle / 360) 
	n = int(arc_lenght / 3) + 1
	step_lenght = arc_lenght / n
	step_angle = float(angle) / n
	polyline(turtle, step_lenght, n, step_angle)

#refatoração da fumção circle:

def circle(turtle, radius):
	arc(turtle, radius, angle = 360)

circle(bob, 100)

turtle.mainloop()