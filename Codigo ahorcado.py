import turtle
import random

#Configuración inicial de la pantalla
pantalla = turtle.Screen()
pantalla.title("Juego del Ahorcado")
pantalla.bgcolor("white")
pantalla.setup(width=600, height=600)

t = turtle.Turtle()
t.hideturtle()
t.speed(3)
t.pensize(3)

# Dibujar la base
def dibujar_horca():
    t.penup()
    t.goto(-150, -150)
    t.pendown()
    t.forward(300) # Base
    t.backward(150)
    t.left(90)
    t.forward(300) # Poste vertical
    t.right(90)
    t.forward(150) # Techo
    t.right(90)
    t.forward(40)  # Cuerda

# Probando la función
dibujar_horca()
turtle.bye()