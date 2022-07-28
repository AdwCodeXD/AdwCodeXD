import turtle
from turtle import*

#Captain America 
#Programmer
#Adwaith Manoj








a = turtle.Turtle()
s = turtle.Screen()


s.bgcolor("white")




penup()
a.goto(0.00,-100)
pendown()
speed(1)
a.color("#9d2d29")
a.begin_fill()
a.circle(120)
a.end_fill()
a.hideturtle()


b = turtle.Turtle()

penup()
b.goto(0.00,-80)
pendown()
speed(1)
b.color("#e1e0e1")
b.begin_fill()
b.circle(100)
b.end_fill()
b.hideturtle()


c = turtle.Turtle()



penup()
c.goto(0.00,-60)
pendown()
speed(1)
c.color("#9d2d29")
c.begin_fill()
c.circle(80)
c.end_fill()
c.hideturtle()



d = turtle.Turtle()


penup()
d.goto(0.00,-40)
pendown()
speed(1)
d.color("#1f67a7")
d.begin_fill()
d.circle(60)
d.end_fill()
d.hideturtle()


penup()
goto(10,39)
pendown()
speed(0)
color("#dbdbdd")
begin_fill()
for i in range(5):
    	forward(40)
    	right(140)
    	forward(40)
    	right(72-140)
end_fill()


penup()
goto(5,33)
pendown()
speed(0)
color("#eceef4")
for i in range(5):
	forward(30)
	right(140)
	forward(30)
	right(72-140)
hideturtle()










#9d2d29






turtle.done()