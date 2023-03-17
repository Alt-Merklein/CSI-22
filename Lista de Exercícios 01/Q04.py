import turtle

def draw_spiral(t,sz, ta):
    side = 0
    while (side < sz):
        t.forward(side)
        t.left(ta)
        side += 2                        # 2 me pareceu mais razoável do que 1


#Por conveniência
def move(t,x,y):                         
    t.penup()
    t.setposition(x,y)
    t.pendown()


wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("spirals")
tess = turtle.Turtle()
tess.color("blue")

move(tess,-200,0)
draw_spiral(tess, 200, 90)
move(tess,200,0)
draw_spiral(tess,200,91)

wn.mainloop()