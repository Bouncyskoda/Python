import turtle


def square(t,d):
	t.pendown()
	t.begin_fill()
	for i in  range (0,4):
		t.fd(d)
		t.rt(90)
	t.end_fill()
	t.penup()
    

def main():
	turtle.tracer(0,0)
	twin = turtle.Screen()
	t = turtle.Turtle()
	#twin.clear()
	count = 0
	for x in range (-400,401,25):
		for y in range (-400,401,25):
			t.penup()
			t.goto(x,y)
			thecolor = "#989898"
			if (count % 12 == 0):
				thecolor = "#64ADF0"
			if (count % 20 == 0):
				thecolor = "#0B27D6"
			if (count % 37 == 0):
				thecolor = "#9E0BD6"
			if (count % 42 == 0):
				thecolor = "#DD591E"
			if (count % 50 == 0):
				thecolor = "#AFE33F"
			if (count % 42 == 0):
				thecolor = "#DD591E"
			t.color(thecolor)
			square(t,20)
			count = count + 1
			print(count)

	turtle.update()
	twin.exitonclick()

if __name__=="__main__":
	main()

