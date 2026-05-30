import turtle
import random

# 1. Configuración inicial de la pantalla
pantalla = turtle.Screen()
pantalla.title("Juego del Ahorcado")
pantalla.bgcolor("white")
pantalla.setup(width=600, height=600)

t = turtle.Turtle()
t.hideturtle() # Ocultamos la flechita
t.speed(3)     # Velocidad del dibujo
t.pensize(3)   # Grosor de la línea

turtle.bye() # Cierra la ventana (temporalmente para probar)