import turtle

example = turtle.Turtle()
example.color("cyan")
example.speed(100)
turtle.bgcolor("black")

colors = ["green", "white", "orange", "navy", "lightblue", "purple", "#D3F122", "lightblue"]


def draw_square():
    for side_a in range(4):
        example.forward(100)
        example.right(90)
        for side_b in range(4):
            example.forward(50)
            example.right(90)


example.penup()
example.back(40)
example.pendown()

for color in colors:
    example.color(color)
    draw_square()
    example.forward(50)
    example.left(45)
example.hideturtle()
turtle.done()
