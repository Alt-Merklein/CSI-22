import turtle

def draw_poly(t,n, sz):
    turn_angle = 360/n
    for i in range(n):
        t.forward(sz)
        t.left(turn_angle)


wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("tess draws a polygon")
tess = turtle.Turtle()
tess.color("red")
draw_poly(tess,8,50)
wn.mainloop()