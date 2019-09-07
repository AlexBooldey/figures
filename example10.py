import turtle

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
example = turtle.Pen()
turtle.bgcolor('black')

for x in range(360):
    example.pencolor(colors[x % 6])
    example.width(x / 100 + 1)
    example.forward(x)
    example.left(59)
