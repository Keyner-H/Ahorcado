import turtle
import random

# Configuración inicial de la pantalla
pantalla = turtle.Screen()
pantalla.title("Juego del Ahorcado")
pantalla.bgcolor("white")
pantalla.setup(width=600, height=600)

t = turtle.Turtle()
t.hideturtle() # Ocultamos la flechita
t.speed(3)     # Velocidad del dibujo (1 es lento, 10 es rápido)
t.pensize(3)   # Grosor de la línea

# Funciones para dibujar (Poco a poco)
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

def dibujar_cabeza():
    t.penup()
    t.goto(0, 70) # Nos posicionamos al final de la cuerda
    t.setheading(0)
    t.pendown()
    t.circle(20)  # Dibujamos la cabeza

def dibujar_cuerpo():
    t.penup()
    t.goto(0, 70)
    t.setheading(270) # Apuntamos hacia abajo
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

# Lista de funciones en orden de los errores
partes_cuerpo = [
    dibujar_cabeza, 
    dibujar_cuerpo, 
    dibujar_brazo_izquierdo, 
    dibujar_brazo_derecho, 
    dibujar_pierna_izquierda, 
    dibujar_pierna_derecha
]

# Lógica del juego
def jugar_ahorcado():
    palabras = ["PYTHON", "PROGRAMACION", "COMPUTADORA", "AHORCADO", "DESARROLLO"]
    palabra_secreta = random.choice(palabras)
    letras_adivinadas = []
    intentos_equivocados = 0
    max_intentos = len(partes_cuerpo)

    # Dibujar la horca al inicio
    t.clear()
    dibujar_horca()

    while intentos_equivocados < max_intentos:
        # Mostrar el progreso de la palabra en la consola o pantalla
        progreso = ""
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                progreso += letra + " "
            else:
                progreso += "_ "
        
        # Si ya no hay guiones bajos el jugador gana
        if "_" not in progreso:
            pantalla.textinput("¡Ganaste!", f"Adivinaste la palabra: {palabra_secreta}\nPresiona OK para salir.")
            break

        # Pedir una letra con una ventana emergente
        intento = pantalla.textinput("Ahorcado", f"Palabra: {progreso}\n\nIngresa una letra:").upper()

        if not intento or len(intento) != 1 or not intento.isalpha():
            continue

        if intento in letras_adivinadas:
            continue # Si ya la puso, la ignoramos

        letras_adivinadas.append(intento)

        if intento not in palabra_secreta:
            # Dibuja el muñequito paso a paso
            partes_cuerpo[intentos_equivocados]() 
            intentos_equivocados += 1

    # Si se acaban los intentos
    if intentos_equivocados == max_intentos:
        pantalla.textinput("¡Perdiste!", f"La palabra era: {palabra_secreta}\nPresiona OK para salir.")

# Iniciar el juego
jugar_ahorcado()
turtle.bye() # Cierra la ventana gráfica al terminar