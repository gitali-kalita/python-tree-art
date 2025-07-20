import turtle
import math

tu = turtle.Turtle()
turtle.bgcolor("light coral")  
tu.pensize(2)
tu.color("sky blue")           
tu.shape("turtle")
tu.speed(0)
tu.left(90)
tu.backward(100)


def draw_hexagon(size):
    tu.begin_fill()
    tu.color("mint cream")    
    for _ in range(6):
        tu.forward(size)
        tu.right(60)
    tu.end_fill()


def tree(i):
    if i < 10:
        draw_hexagon(8)
        return
    else:
        tu.forward(i)
        tu.color("light cyan")
        draw_hexagon(5)
        tu.color("steel blue")
        tu.left(30)
        tree(int(i * 0.65))
        tu.right(60)
        tree(int(i * 0.65))
        tu.left(30)
        tu.backward(i)


tree(100)
turtle.done()