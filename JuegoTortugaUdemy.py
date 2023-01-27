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
turtleOne.circle(40)
# regrasar la totuga en el sitio de partida dejamos de dibujar
turtleOne.penup()
# le damos las coordenadas donde se ubicará la tortuga
turtleOne.goto(-250,225)


turtleTwo.penup()
# desplazar jugador uno a un lugar especifico
turtleTwo.goto(200,-200)
#ordenar que empice a dibujar
turtleTwo.pendown()
#ordenamos crear la casa con el circulo
turtleTwo.circle(40)
# regrasar la totuga en el sitio de partida dejamos de dibujar
turtleTwo.penup()
# le damos las coordenadas donde se ubicará la tortuga
turtleTwo.goto(-250,-170)



turtle.done()

