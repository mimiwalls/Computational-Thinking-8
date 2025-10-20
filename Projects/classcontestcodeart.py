import turtle
t = turtle.Turtle()
turtle.Screen().bgcolor("Navy")
t.goto(100, 0)
t.color("cyan")
t.speed(500)
#this is making the first one
for i in range(270):
    t.forward(200)
    t.left(197)
#this is making another one
#i changed the color here and made the speed different here as well
t.color("purple")
t.speed(5000)
for i in range(270):
    t.forward(200)
    t.left(197)
    t.right(10)
    t.left(300)
    t.forward(40)
#this is making another one
t.color("pink")
#this controls the speed
t.speed(5000)
for i in range(300):
    t.forward(600)
    t.left(600)
    t.right(600)
    t.left(600)
turtle.exitonclick()