import turtle

t = turtle.Turtle()

t.color("red", "yellow")
t.speed(10)

t.begin_fill()
for i in range(100):
    t.forward(200)
    t.left(168.5)
t.end_fill()

turtle.done()
