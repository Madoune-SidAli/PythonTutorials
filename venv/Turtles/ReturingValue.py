import turtle

t = turtle.Turtle()
t.color("red")
t.width(1)
t.speed(0)
t.hideturtle()

def square(number):
    return number * number

for n in range(540):
    angle = square(n)
    t.right(angle + .5)
    t.forward(5)

""" The Second part of returning a value was about:
# Fill out the function bead_color.
# It should return color names so that the
# chain of beads will alternate among red,
# green, and blue.

import turtle

def bead_color(num):
    if num % 3 == 0:
        return "red"
    else:
        if num % 3 == 1 :
            return "green"
    return "blue"

def bead(tur):
    tur.right(75)
    for _ in range(12):
        tur.forward(10)
        tur.left(30)
    tur.left(75)  """
