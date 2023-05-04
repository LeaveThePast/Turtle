import turtle

colors = ['silver', 'gray', 'black']
colorss = ['gray', 'black', 'silver']

draw = turtle.Pen()
turtle.bgcolor('white')
draw.speed(1000)

for a in range(360):
    draw.pencolor(colors[a%3])
    draw.width(a/100+2)
    draw.forward(a)
    draw.left(-180)
    draw.right(30)


if __name__ == '__main__':
    draw.hideturtle()
