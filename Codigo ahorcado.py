import turtle
import random

pantalla = turtle.Screen()
pantalla.title("Juego del Ahorcado")
pantalla.bgcolor("white")
pantalla.setup(width=600, height=600)

t = turtle.Turtle()
t.hideturtle()
t.speed(3)
t.pensize(3)

#Partes del cuerpo funciones

def dibujar_horca():
    t.penup()
    t.goto(-150, -150)
    t.pendown()
    t.forward(300)
    t.backward(150)
    t.left(90)
    t.forward(300)
    t.right(90)
    t.forward(150)
    t.right(90)
    t.forward(40)

def dibujar_cabeza():
    t.penup()
    t.goto(0, 70)
    t.setheading(0)
    t.pendown()
    t.circle(20)

def dibujar_cuerpo():
    t.penup()
    t.goto(0, 70)
    t.setheading(270)
    t.pendown()
    t.forward(80)

def dibujar_brazo_izquierdo():
    t.penup()
    t.goto(0, 40)
    t.setheading(225)
    t.pendown()
    t.forward(50)

def dibujar_brazo_derecho():
    t.penup()
    t.goto(0, 40)
    t.setheading(315)
    t.pendown()
    t.forward(50)

def dibujar_pierna_izquierda():
    t.penup()
    t.goto(0, -10)
    t.setheading(225)
    t.pendown()
    t.forward(60)

def dibujar_pierna_derecha():
    t.penup()
    t.goto(0, -10)
    t.setheading(315)
    t.pendown()
    t.forward(60)

partes_cuerpo = [dibujar_cabeza, dibujar_cuerpo, dibujar_brazo_izquierdo, dibujar_brazo_derecho, dibujar_pierna_izquierda, dibujar_pierna_derecha]

dibujar_horca()
for parte in partes_cuerpo:
    parte()

turtle.bye()