import random
import turtle

num_str = input("Enter the side number of the shape you want to draw: ")
squares = int(num_str)

angle = 180 - 180 * (squares - 2) / squares
example = turtle.Turtle()
turtle.bgcolor("black")

x = 0
y = 0
example.setpos(x, y)

for x in range(8):
    example.color(random.random(), random.random(), random.random())
    x += 5
    y += 5
    example.forward(x)
    example.left(y)
    for i in range(squares):
        example.begin_fill()
        example.down()
        example.forward(40)
        example.left(angle)
        example.forward(40)
        print(example.pos())
        example.up()
        example.end_fill()

turtle.done()
