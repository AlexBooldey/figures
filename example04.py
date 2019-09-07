import turtle


def spiral(sides, trun, color, width):
    example = turtle.Turtle()
    example.color(color)
    example.speed(100)
    example.width(width)

    for n in range(sides):
        example.forward(n)
        example.right(trun)


spiral(150, 45, "cyan", 5)
turtle.done()
