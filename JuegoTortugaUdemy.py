import turtle

# Pantalla

s = turtle.Screen()
# titulo de pantalla "carrera de tortugas"
s.title("turtle race") 
#Cambiar color de pantalla
s.bgcolor("grey")


#crear Jugadores

turtleOne = turtle.Turtle()
turtleTwo = turtle.Turtle()

#Jugador Uno

#para que al crear la casa no se vea la tortuga o el jugador
turtleOne.hideturtle()
# darle forma de tortuga 
turtleOne.shape("turtle")
#cambiar el color
turtleOne.color("green","green")
#cambiar el tamaño
turtleOne.shapesize(2,2,2)
# dar grosor a la tinta o la pluma
turtleOne.pensize(4)


# Crear jugador dos

#para que al crear la casa no se vea la tortuga o el jugador
turtleTwo.hideturtle()
# darle forma de tortuga
turtleTwo.shape("turtle")
#cambiar el color
turtleTwo.color("blue", "blue")
#cambiar el tamaño
turtleTwo.shapesize(2,2,2)
# dar grosor a la tinta o la pluma
turtleTwo.pensize(4)




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
# para que aparescan el juador uno
turtleOne.showturtle()
# para que aparescan el juador dos
turtleTwo.showturtle()



turtle.done()

