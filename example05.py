import turtle

example = turtle.Turtle()
example.color("cyan")
example.speed(100)
turtle.bgcolor("black")


def draw_square(length):
    for side_a in range(4):
        example.forward(length)
        example.right(90)
        for side_b in range(4):
            example.forward(50)
            example.right(90)


example.penup()
example.back(20)
example.pendown()

for square in range(80):
    draw_square(5)
    example.forward(5)
    example.left(5)

example.hideturtle()
turtle.done()
