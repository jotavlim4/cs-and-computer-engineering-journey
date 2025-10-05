import turtle

def draw(t, lenght, n):
	if n == 0:
		return
	angle = 50
	t.fd(lenght * n)
	t.lt(angle)
	draw(t, lenght,n - 1)
	t.rt(2 * angle)
	draw(t, lenght,n - 1)
	t.lt(angle)
	t.bk(lenght * n)


if __name__ == '__main__':
	bob = turtle.Turtle()
	draw(bob, 20, 2)
	turtle.mainloop()