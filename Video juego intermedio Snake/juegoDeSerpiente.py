import turtle
import time
import random

#la serpiente debe moverse cada cierto retrazo(delay) en este caso 1 segun do
delayTime = 0.1


#crear pantalla 
s = turtle.Screen()
#darle un tamaño a la pantalla que por defecto viene de 500 X 500
s.setup(650,650)
# cambiar color
s.bgcolor('gray')
s.title('Juego de Serpiente')

#crear jugador
serpirte  = turtle.Turtle()
#darle rapidez a la serpiente con speed que va del 1 al 10
serpirte.speed(1)
#darle forma a la serpiente(cuadrado)
serpirte.shape('square')
#hacer que no se dibuje el reorrido de la serpiente
serpirte.penup()
#punto de inicio de la serpiente
serpirte.goto(0,0)

# hacer que al reiniciar eljuego la serpiente se quede en el punto de inicio

serpirte.direction = "stop"
#darle color
serpirte.color("blue")

#crear la comida

meal = turtle.Turtle()
meal.shape("circle")
meal.color("red")
meal.penup()
meal.goto(0,100)
#rapidez
meal.speed(0)

# creamos una lista vacia para alargar el cuerpo de la serpiente con varios segmentos
bodySerpirte = []



#darle movimiento a la serpiente

# dar movimiento a la serpiente con el teclado cambiando el valor de serpiente.direction

#hacia arriba
def upwards():
   serpirte.direction = "up" 

   #hacia abajo
def below():
   serpirte.direction = "down" 

   #hacia la derecha
def onTheRight():
   serpirte.direction = "right" 

   #hacia izquierda
def onTheLeft():
   serpirte.direction = "left" 


# crear la función del movimiento
def motion():
    #creamos la condicional si la serpiente 
   
    # se mueve hacia arriba
    if serpirte.direction == "up":
        #creamos la variable y
        y = serpirte.ycor()
        #aplicamos la función sety para mover le serpiente en el eje de las y + 20 pixeles
        serpirte.sety(y + 20)
 

    # se mueve hacia abajo
    if serpirte.direction == "down":
        #creamos la variable y
        y = serpirte.ycor()
        #aplicamos la función sety para mover le serpiente en el eje de las y + 20 pixeles
        serpirte.sety(y -20)

 
    # se mueve hacia derecha
    if serpirte.direction == "right":
        #creamos la variable x
        x = serpirte.xcor()
        #aplicamos la función sety para mover le serpiente en el eje de las y + 20 pixeles
        serpirte.setx(x + 20)

    # se mueve hacia izquierda
    if serpirte.direction == "left":
        #creamos la variable x
        x = serpirte.xcor()
        #aplicamos la función sety para mover le serpiente en el eje de las y + 20 pixeles
        serpirte.setx(x - 20)

 #llamar alas teclas

 #poner en escucha los eventos del teclado
s.listen()
#evento escuche  tecla presionada arriba del teclado s.keypress(nombre dela funcion, evento del teclado "Up")
s.onkeypress(upwards, "Up")
s.onkeypress(below, "Down")
s.onkeypress(onTheRight, "Right")
s.onkeypress(onTheLeft, "Left")



#aplicamos un while True para asegurase de que siempre se repita ya que normalmente los juegos tienen un bucle llamado loop que se repite constantemente ya que cada vez que un jugador se mueve debe actualizarse lo que se muestra en pantalla

while True:
    #actualizar pantalla
    s.update()
    #función para parar cuando la serpiente toque los bordes
    if serpirte.xcor() > 300 or serpirte.xcor() < -300 or serpirte.ycor() > 300 or serpirte.ycor() < -300:
        #para que se detenga o haga una pequeña pausa y reinicie el juego
        time.sleep(2)
        # recorrer los elementos de la lista bodyserpirte
        for i in bodySerpirte:
            #eliminar cada uno de los elementos de la lista
            i.clear()

            i.hideturtle()
         #enviar serpiente al punto de inicio
        serpirte.home()
        #mantenert la serpuiente en stop hasta que presione una tecla
        serpirte.direction = "stop"

        bodySerpirte.clear()



#para que la comida se movilice a un lugar rando
#cuando la distacia sea menor a 20 que es la distacia que de movera la serpiente

    if serpirte.distance(meal) < 20:

        #escoger dirección aleatoria en el eje de las x
        motionX = random.randint(-250,250)

           #escoger dirección aleatoria en el eje de las x
        motionY = random.randint(-250,250)

        meal.goto(motionX,motionY)

        # creamos los nuevos segmentos que alargaran el cuerpo de la serpiente
        newBodySerpirte = turtle.Turtle()
        newBodySerpirte.shape("square")
        newBodySerpirte.color("blue")
        newBodySerpirte.penup()
        newBodySerpirte.goto(0,100)
        newBodySerpirte.speed(0)
        #agregar el nuevo cuerpo a la lista bodySerpirte
        bodySerpirte.append(newBodySerpirte)
        #creamos la variable total  que va ser igual al tamaño del cuerpo
    total =  len(bodySerpirte)
        #recorremos la lista con un for que inicie con -1 para recorer la lista a la inversa, el 0 para que no lo cuente, -1 para que la cuenta vaya de 1 en 1
    for i in range(total -1,0,-1):
         #para iniciar las coordenadas x y desde cero
        x = bodySerpirte[i-1].xcor()
        y = bodySerpirte[i-1].ycor()
         # enviar el cuerpo a la cabeza de la serpiente
        bodySerpirte[i].goto(x,y)
        #si en la lista no está vacia
    if total > 0:
        x = serpirte.xcor()
        y = serpirte.ycor()
        bodySerpirte[0].goto(x,y)
  
    # llamamos la función movimiento
    motion()
    #para que la serpiente atrace el recorrido ya
    for i in bodySerpirte:
        if i.distance(serpirte) < 20:
            for i in bodySerpirte:
                i.clear()

                i.hideturtle()
             #enviar serpiente al punto de inicio
            serpirte.home()
            bodySerpirte.clear()   
            #mantenert la serpuiente en stop hasta que presione una tecla
            serpirte.direction = "stop"

            
    time.sleep(delayTime)


turtle.done()