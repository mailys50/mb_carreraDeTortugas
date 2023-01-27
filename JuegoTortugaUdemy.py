import turtle

s = turtle.Screen()
s.title("carrera de tortuga")
turtleOne = turtle.Turtle()
turtleTwo = turtle.Turtle()
# darle forma de tortuga y color a la pluma al jugador 1
turtleOne.shape("turtle")
turtleOne.color("green","green")
# darle forma de tortuga y color a la pluma al jugador 2
turtleTwo.shape("turtle")
turtleTwo.color("blue", "blue")
# dejar de dibujar
turtleOne.penup()
# desplazar jugador uno a un lugar especifico
turtleOne.goto(200,200)
#ordenar que empice a dibujar
turtleOne.pendown()
#ordenamos crear la casa con el circulo
turtleOne.circle(30)





turtle.done()

