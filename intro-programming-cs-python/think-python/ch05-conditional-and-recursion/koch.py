import turtle

def koch(t, lenght):
	if lenght < 3:
		t.forward(lenght)
	else:
		angle = 60
		koch(t, lenght/3)
		t.left(angle)
		koch(t, lenght/3)
		t.right(2 * angle)
		koch(t, lenght/3)
		t.left(angle)
		koch(t, lenght/3)

def snowflake(t, lenght, n):
	angle = 60
	for i in range(n):
		koch(t, lenght)
		t.right(angle * 2)

def minkowski(t, lenght):
	if lenght < 5:
		t.forward(lenght)
	else:
		angle = 90
		minkowski(t, lenght/4)
		t.left(angle)
		minkowski(t, lenght/4)
		t.right(angle)
		minkowski(t, lenght/4)	
		t.right(angle)
		minkowski(t, lenght/4)
		minkowski(t, lenght/4)
		t.left(angle)
		minkowski(t, lenght/4)
		t.left(angle)
		minkowski(t, lenght/4)
		t.right(angle)
		minkowski(t, lenght/4)

if __name__ == '__main__':
	bob = turtle.Turtle()
	bob.speed(10)
	# koch(bob, 12000)
	# snowflake(bob, 120, 3)
	minkowski(bob, 300)
	turtle.mainloop()
