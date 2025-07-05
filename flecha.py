import turtle

turtle = turtle.Turtle()
turtle.speed(2)

turtle.penup()
turtle.goto(-200, 50) 
turtle.setheading(0)  
turtle.pendown()

# Línea punteada
for _ in range(10):
    turtle.pendown()
    turtle.forward(10)
    turtle.penup()
    turtle.forward(5)

# Flecha
turtle.pendown()
turtle.left(150)
turtle.forward(20)
turtle.back(20)
turtle.right(300)
turtle.forward(20)
turtle.back(20)
turtle.left(150)

#Mover 
turtle.penup()
turtle.goto(-200, -50)
turtle.setheading(0)
turtle.pendown()

# Línea punteada
for _ in range(10):
    turtle.pendown()
    turtle.forward(20)
    turtle.penup()
    turtle.forward(5)

# Flecha
turtle.pendown()
turtle.left(150)
turtle.forward(20)
turtle.back(20)
turtle.right(300)
turtle.forward(20)
turtle.back(20)
turtle.left(150) 

