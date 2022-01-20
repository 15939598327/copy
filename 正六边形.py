import turtle


def draw_triangle(n):
    turtle.color("green")
    turtle.begin_fill()
    for i in range(3):
        turtle.fd(n)
        turtle.left(120)
    turtle.end_fill()


turtle.hideturtle()
# 六边形
turtle.color("red")
turtle.begin_fill()
turtle.left(60)
turtle.fd(150)
for j in range(5):
    turtle.right(60)
    turtle.fd(150)
turtle.end_fill()

# 三角形
turtle.right(60)
draw_triangle(150)
for k in range(5):
    turtle.fd(150)
    turtle.right(60)
    draw_triangle(150)
turtle.mainloop()
