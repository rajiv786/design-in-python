import turtle
def rectangle(color):
    t.begin_fill()
    t.fillcolor(color)
    for i in range(2):
        t.forward(400)
        t.right(90)
        t.forward(40)
        t.right(90)
        t.end_fill()
t=turtle.Turtle()
t.up()
t.goto(0,-300)
t.down()
t.goto(0,400)
rectangle("orange")
t.goto(0,300)
rectangle("white")
t.goto(0,200)
rectangle("green")


