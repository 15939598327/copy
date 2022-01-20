import turtle


def circle():
    turtle.fd(100)
    turtle.left(90)
    turtle.circle(100, 45)
    turtle.goto(0, 0)


turtle.hideturtle()
color = ["blue", "green", "red"]
turtle.color("black", "yellow")
turtle.begin_fill()
turtle.left(45)
circle()
turtle.end_fill()

for i in range(3):
    turtle.color("black", color[i])
    turtle.begin_fill()
    turtle.right(45)
    circle()
    turtle.end_fill()
turtle.mainloop()
