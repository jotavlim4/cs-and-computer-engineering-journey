import math
import turtle

bob = turtle.Turtle()

def polyline(turtle, n, length, angle):
    for i in range(n):
        turtle.fd(length)
        turtle.lt(angle)
        print(f"iteração: {i}")

def arc(turtle, radius, angle):
    arc_lenght = 2 * math.pi * radius * (angle / 360)
    n = int(arc_lenght / 3) + 1
    step_lenght = arc_lenght / n
    step_angle = float(angle / n)

    print(f"arc_lenght: {arc_lenght}")
    print(f"n: {n}")
    print(f"step_angle: {step_angle}")
    print(f"step_lenght: {step_lenght}")

    polyline(turtle, n, step_lenght, step_angle)


def circle(turtle, radius):
    arc(turtle, radius, angle = 360)

circle(bob, 100)

turtle.mainloop()
