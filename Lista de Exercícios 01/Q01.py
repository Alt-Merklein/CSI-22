import turtle

def draw_square(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Alex draws some squares")
alex = turtle.Turtle()
alex.color("red")

center = alex.pos()
for i in range(1,6):
    startPos = center + (-10*i, -10*i)
    alex.penup()
    alex.setposition(startPos)
    alex.pendown()
    draw_square(alex, 20 * i)

wn.mainloop()
