import turtle

turtle = turtle.Turtle()
turtle.speed(2)

#Triángulo
turtle.penup()
turtle.goto(-300, 0)
turtle.setheading(0)
turtle.pendown()

turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)

#Rectángulo
turtle.penup()
turtle.goto(-100, 0)
turtle.setheading(0)
turtle.pendown()

turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)

#Hexagono
turtle.penup()
turtle.goto(150, 0)
turtle.setheading(0)
turtle.pendown()

for _ in range(3):
    turtle.forward(120) 
    turtle.left(60)   
    turtle.forward(150) 
    turtle.left(60)  
