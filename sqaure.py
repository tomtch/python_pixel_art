import turtle
from datetime import datetime
from tkinter import Image

t = turtle.Turtle()
t.color("#3C9118", "cyan")

t.begin_fill()
for x in range(1,4):
    t.forward(100)
    t.left(90)
t.forward(100)
t.end_fill()

t.penup()
t.forward(150)
t.left(90)

t.pendown()
t.begin_fill()
for x in range(1,4):
    t.forward(100)
    t.left(90)
t.forward(100)
t.end_fill()

turtle.done()
