import random
import turtle


def hue_gen(hue=0, val=1, sat=1):
    if 0 <= hue < 60:
        r = 1
        g = (hue / 59) + (1 - sat) * (59 - hue) / 59
        b = 1 - sat
        hue_out = (r * val, g * val, b * val)
    elif 60 <= hue < 120:
        r = ((1 - (hue - 60) / 59) + (1 - sat) * (1 - (119 - hue) / 59))
        g = 1
        b = 1 - sat
        hue_out = (r * val, g * val, b * val)
    elif 120 <= hue < 180:
        r = 1 - sat
        g = 1
        b = ((hue - 120) / 59) + (1 - sat) * (179 - hue) / 59
        hue_out = (r * val, g * val, b * val)
    elif 180 <= hue < 240:
        r = 1 - sat
        g = (1 - (hue - 180) / 59) + (1 - sat) * (1 - (239 - hue) / 59)
        b = 1
        hue_out = (r * val, g * val, b * val)
    elif 240 <= hue < 300:
        r = ((hue - 240) / 59) + (1 - sat) * (299 - hue) / 59
        g = 1 - sat
        b = 1
        hue_out = (r * val, g * val, b * val)
    elif 300 <= hue < 360:
        r = 1
        g = 1 - sat
        b = (1 - (hue - 300) / 59) + (1 - sat) * (1 - (359 - hue) / 59)
        hue_out = (r * val, g * val, b * val)
    elif hue >= 360:
        hue_out = hue_gen(hue % 360, val, sat)
    return hue_out


def time_tunnel(repeats=1, zigzag=10, step=1, curve=0):
    for i in range(repeats):
        example.goto(0, 0)
        example.seth(random.uniform(0, 360))  # set heading
        h1 = example.heading()  # get heading
        example.color(hue_gen(hue=i))
        for j in range(50):
            example.down()
            example.forward(abs(round(random.gauss(2, step), 0)))  # abs limits motion to forward
            example.seth(h1 + curve * j + random.gauss(0, 4 * zigzag))
            x = example.xcor()
            y = example.ycor()
            example.color(hue_gen(hue=i * j, val=j / 50))  # 1 - 51
            h2 = example.heading()
        for k in range(2):
            example.down()
            example.seth(h2)
            for k2 in range(50):
                example.color(hue_gen(hue=i + j + k * k2, val=k2 / 50))
                example.seth(h2 + curve * k2 + random.gauss(0, 2 * zigzag))
                example.forward(abs(round(random.gauss(2, step), 0)))
            example.up()
            m = example.xcor()
            n = example.ycor()
            h3 = example.heading()
            # h4 = alex.heading()
            for l in range(4):
                example.color(hue_gen(hue=9 * l))
                example.down()
                example.seth(h3)
                # h5 = alex.heading()
                for l2 in range(50):
                    example.color(hue_gen(hue=l * l2 * 2.449, val=l2 / 50))
                    example.seth(h3 + curve * l2 + random.gauss(0, zigzag))
                    example.forward(abs(round(random.gauss(2, step), 0)))
                example.up()
                example.goto(m, n)
            example.goto(x, y)
        example.up()


turtle.tracer(0, 0)
wn = turtle.Screen()
wn.colormode(1)
turtle.bgcolor("black")
example = turtle.Turtle()
example.speed(10)
example.pensize(0)
example.ht()
time_tunnel(500, 1, 1, .5)
turtle.update()
wn.exitonclick()
