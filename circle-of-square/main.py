import turtle

window = turtle.Screen()

t = turtle.Turtle()
t.speed(0)

def square(size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

def circle(count, right):
    for _ in range(count):
        square(100)
        t.right(right)

circle(100, 5)

window.exitonclick()