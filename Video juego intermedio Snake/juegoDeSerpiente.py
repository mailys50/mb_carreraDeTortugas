import turtle
import time

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
serpirte.direction = "left"
#darle color
serpirte.color("blue")



#darle movimiento a la serpiente
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

 


#aplicamos un while True para asegurase de que siempre se repita ya que normalmente los juegos tienen un bucle llamado loop que se repite constantemente ya que cada vez que un jugador se mueve debe actualizarse lo que se muestra en pantalla

while True:
    #actualizar pantalla
    s.update()
    # llamamos la función movimiento
    motion()
    #para que la serpiente atrace el recorrido ya
    time.sleep(delayTime)


turtle.done()