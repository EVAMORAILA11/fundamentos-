import turtle

# Dibujar el cuadrado (lado 100)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)

turtle.penup() #subir lapiz 
turtle.goto(0, 0)  #llevo a la esquina
turtle.pendown() #baja lapiz 

turtle.goto(100, 100)

turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
turtle.goto(100, 0)

turtle.penup()
turtle.goto(0, 100)
turtle.pendown()


# triángulo
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)




turtle.done()



