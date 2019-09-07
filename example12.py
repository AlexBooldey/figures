import random
import turtle


def color_gen(sat=1, val=1):
    rand1 = round(random.randrange(256) * val)
    rand2 = round(random.randrange(256) * val)
    sat2 = round((1 - sat) * 255)
    if rand1 >= rand2:
        rand1 = round(255 * val)
    else:
        rand2 = round(255 * val)
    color = [[sat2, rand1, rand2], [rand1, sat2, rand2], [sat2, rand2, rand1],
             [rand1, rand2, sat2], [rand2, sat2, rand1], [rand2, rand1, sat2]]
    return tuple(color[random.randrange(6)])


def time_tunnel(repeats=1, zigzag=10, step=1):
    for i in range(repeats):
        example.goto(0, 0)
        example.seth(random.uniform(0, 360))  # set heading
        h1 = example.heading()  # get heading
        example.color(color_gen(val=0))
        for j in range(10):
            example.down()
            example.forward(abs(round(random.gauss(10, step), 0)))  # abs limits motion to forward
            example.seth(h1 + random.gauss(0, zigzag))
            x = example.xcor()
            y = example.ycor()
            example.color(color_gen(val=j / 10))
            h2 = example.heading()
        for k in range(3):
            example.down()
            example.seth(h2 + random.gauss(0, zigzag))
            h3 = example.heading()
            for k2 in range(10):
                example.color(color_gen(val=k2 / 10))
                example.seth(h3 + random.gauss(0, zigzag))
                example.forward(abs(round(random.gauss(10, step), 0)))
            example.up()
            m = example.xcor()
            n = example.ycor()
            h4 = example.heading()
            for l in range(2):
                example.color(color_gen())
                example.down()
                example.seth(abs(h4 + random.gauss(0, zigzag)))
                h5 = example.heading()
                for l2 in range(10):
                    example.color(color_gen(val=l2 / 10))
                    example.seth(h5 + random.gauss(0, zigzag))
                    example.forward(abs(round(random.gauss(10, step), 0)))
                example.up()
                example.goto(m, n)
            example.goto(x, y)
        example.up()


turtle.tracer(0, 0)
wn = turtle.Screen()
wn.colormode(255)
turtle.bgcolor("black")
example = turtle.Turtle()
example.speed(10)
example.pensize(0)
example.ht()
time_tunnel(300)
turtle.update()
wn.exitonclick()
