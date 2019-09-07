import turtle


def spiral(sides, trun, color, width):
    example = turtle.Turtle()
    example.color(color)
    example.width(width)
    example.speed(100)

    for n in range(sides):
        example.forward(n)
        example.right(trun)

        example.penup()
        example.left(60)
        example.forward(10)
        example.right(60)
        example.pendown()

        example.hideturtle()


turtle.bgcolor("black")
spiral(150, 45, "cyan", 5)
turtle.done()
