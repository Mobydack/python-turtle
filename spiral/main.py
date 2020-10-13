import turtle
import square

def main():
    t = turtle.Turtle()
    t.speed(0)
    size: int = 2

    for _ in range(1000):
        square.print(size, t)
        t.right(5)

        size += 2

if __name__ == "__main__":
    window = turtle.Screen()
    main()
    window.exitonclick()