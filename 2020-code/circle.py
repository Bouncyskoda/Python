import turtle

def draw_circle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()
    turtle.pendown()

tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(5)

draw_circle(tommy, "green", 50, 25, 0)
draw_circle(tommy, "blue", 40, 0, 0)
draw_circle(tommy, "yellow", 30, -25, 0)
draw_circle(tommy, "black" , 20, -50, 0)
draw_circle(tommy, "purple" , 18, -60, 10)
draw_circle(tommy, "lime" , 17, -70, 11)
draw_circle(tommy, "orange" , 16, -70, 15)
draw_circle(tommy, "blue violet" , 15, -70, 23)
draw_circle(tommy, "red" , 14, -70, 8)
draw_circle(tommy, "aqua" , 13, -70, 5)
draw_circle(tommy, "navy" , 12, -70, 1)
draw_circle(tommy, "indigo" , 11, -70, -3)
draw_circle(tommy, "amber" , 10, -70, -6)
draw_circle(tommy, "pink" , 9, -70, -2)
draw_circle(tommy, "grey" , 8, -70, 2)
draw_circle(tommy, "teal" , 7, -70, 7)

