import turtle

t = turtle.Turtle()
t.color("red", "yellow")

t.begin_fill()
for i in range(4):
    for i in range(8):
        t.forward(200)
        t.left(135)

    t.right(90)
t.end_fill()

turtle.done()
