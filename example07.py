import turtle

example = turtle.Turtle()
example.color("cyan")
example.speed(100)

for side in range(19):
    example.forward(10 * side)
    example.right(360 / 3)

example.hideturtle()
turtle.done()
