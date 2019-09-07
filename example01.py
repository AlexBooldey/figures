import turtle

example = turtle.Turtle()
example.color("misty rose")
example.speed(100)


def draw_square():
    for side_a in range(4):
        example.forward(100)
        example.right(90)
        for side_b in range(4):
            example.forward(50)
            example.right(90)


example.penup()
example.back(20)
example.pendown()

for square in range(80):
    draw_square()
    example.forward(5)
    example.left(5)
example.hideturtle()
