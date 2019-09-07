import turtle

example = turtle.Turtle()
example.color("cyan")
example.speed(100)

colors = ["green", "black", "orange", "navy", "lightblue", "purple", "#D3F122", "lightblue"]


def draw_square():
    for side_a in range(4):
        example.forward(100)
        example.right(90)
        for side_b in range(4):
            example.forward(50)
            example.right(90)


draw_square()


def new_function():
    for square in range(8):
        draw_square()
        example.penup()
        example.forward(20)
        example.left(45)
        example.pendown()


new_function()
turtle.done()
