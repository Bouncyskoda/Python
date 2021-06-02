# recursion
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
	twin = turtle.Screen()
	t = turtle.Turtle()
	#twin.clear()
	t.penup()
	t.goto(0,0)
	t.color("#000000")
	square(t,20)
	t.goto(0,10)
	t.color("#0000ff")
	square(t,20)
	t.goto(1,13)
	t.color("#791FDE")# F6 10 10
	square(t,20)
	t.goto(2,17)
	t.color("#B13CD4")
	square(t,20)
	t.goto(5,24)
	t.color("#D324CE")
	square(t,20)
	t.goto(7,30)
	t.color("#EA1E91")
	square(t,20)
	t.goto(10,36)
	t.color("#E02465")
	square(t,20)
	t.goto(12,40)
	t.color("#FF0E07")
	square(t,20)
	t.goto(15,44)
	t.color("#E5581E")
	square(t,20)
	t.goto(18,51)
	t.color("#FF7E00")
	square(t,20)
	t.goto(23,59)
	t.color("#F2BC1C")
	square(t,20)
	t.goto(27,63)
	t.color("#E6F21C")
	square(t,20)
	t.goto(30,67)
	t.color("#9DF21C")
	square(t,20)
	t.goto(36,67)
	t.color("#38DE07")
	square(t,20)
	t.goto(40,67)
	t.color("#4BEE5F")
	square(t,20)
	t.goto(50,57)
	t.color("#54D589")
	square(t,20)
	t.goto(56,54)
	t.color("#52C6CA")
	square(t,20)
	t.goto(56,54)
	t.color("#5CD6FF")
	square(t,20)
	
	twin.exitonclick()

if __name__=="__main__":
	main()



'''
for n in range (1,20):
		t.goto(0,n*22)
		square(t,20)
#turtle.tracer(0, 0)


	#print(dist)
#turtle.update()

https://docs.python.org/2/library/turtle.html#turtle.delay

screen.tracer(8, 25)
>>> dist = 2
>>> for i in range(200):
...     fd(dist)
...     rt(90)
...     dist += 2

'''