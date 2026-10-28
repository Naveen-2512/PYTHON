import turtle

def draw_koch(pen, length, level):
    # Base condition
    if level == 0:
        pen.forward(length)
    else:
        draw_koch(pen, length / 3, level - 1)
        pen.left(60)

        draw_koch(pen, length / 3, level - 1)
        pen.right(120)

        draw_koch(pen, length / 3, level - 1)
        pen.left(60)

        draw_koch(pen, length / 3, level - 1)


def draw_snowflake(pen, length, level):
    # Draw three Koch curves
    for i in range(3):
        draw_koch(pen, length, level)
        pen.right(120)


def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=700)
    screen.title("Koch Snowflake Fractal Generator")
    screen.bgcolor("black")

    pen = turtle.Turtle()
    pen.speed(0)
    pen.pensize(2)
    pen.color("cyan")

    length = int(input("Enter snowflake size (e.g. 300): "))
    level = int(input("Enter recursion level (0 to 4): "))

    if length <= 0 or level < 0 or level > 4:
        print("Enter a positive size and recursion level from 0 to 4.")
        screen.bye()
        return

    pen.penup()
    pen.goto(-length / 2, length / 3)
    pen.pendown()

    draw_snowflake(pen, length, level)

    turtle.done()


if __name__ == "__main__":
    main()
