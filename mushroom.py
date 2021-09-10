from turtle import Turtle, backward

t = Turtle()
side = 10
t.width(1)
numSquares = 16


def drawSquare(color):
    t.color(color)
    t.begin_fill()
    for i in range(4):
        t.forward(side)
        t.right(90)
    t.end_fill()
    t.forward(side)

def nextRow():
    t.penup()
    t.backward(numSquares * side)
    t.left(90)
    t.forward(side)
    t.right(90)
    t.pendown()

# def draw():


