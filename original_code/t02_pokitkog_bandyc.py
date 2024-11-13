import turtle

wn = turtle.Screen()
galina = turtle.Turtle()
galina.pensize(5)

cody = turtle.Turtle()
cody.pensize(5)

#code for initial G
galina.left(90)
galina.forward(50)
galina.left(90)
galina.forward(50)
galina.left(90)
galina.forward(150)
galina.left(90)
galina.forward(75)
galina.left(90)
galina.forward(65)
galina.left(90)
galina.forward(35)

#code for initial P
galina.penup()
galina.left(180)
galina.forward(80)
galina.right(90)
galina.forward(70)
galina.left(180)
galina.pendown()

galina.forward(150)
galina.right(90)
galina.forward(50)
galina.right(90)
galina.forward(75)
galina.right(90)
galina.forward(50)

#code for initial C
cody.penup()
cody.forward(200)
cody.left(90)
cody.forward(50)
cody.right(90)
cody.forward(50)

cody.left(180)
cody.pendown()
cody.forward(50)
cody.left(90)
cody.forward(150)
cody.left(90)
cody.forward(50)

#code for initial B
cody.penup()
cody.forward(50)
cody.pendown()
cody.left(90)
cody.forward(155)
cody.right(135)
cody.forward(55)
cody.right(90)
cody.forward(55)
cody.left(90)
cody.forward(55)
cody.right(90)
cody.forward(55)


wn.exitonclick()
