import turtle 
import math 
import random

#twin = turtle.Screen()
#twin.clear()
#t = turtle.Turtle()

#t.penup()
#.goto(0,0)
#t.pendown()

def arcR(t,x,y,l,tn,h):
	t.down()
	#t.adam(h)
	for i in range(1,10):
		t.forward(l)
		t.rt(tn)

def sheld(t):
	t.goto(100,-400)
	t.pendown()
	t.rt(180)
	t.begin_fill()
	tcolor = "#ff0000";t.color(tcolor)
	arcR(t,x,y,300,40,90)
	t.end_fill()
	
if __name__ == "__main__":
	x = -400; y = 0
	w = turtle.Screen()
	w.setup(1000,1000)
	w.clear()
	w.bgcolor("#ffffff")
	t = turtle.Turtle()
	sheld(t)
	w.exitonclick()