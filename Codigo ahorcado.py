# ahorcado.py
import turtle
import random

class JuegoAhorcado:
    """
    Juego del Ahorcado implementado con Programación Orientada a Objetos
    usando la librería turtle de Python.
    """

    def __init__(self):
        # --- Configuración de la ventana ---
        self.pantalla = turtle.Screen()
        self.pantalla.title("El Ahorcado - POO con Turtle")
        self.pantalla.bgcolor("#1e1e2e")
        self.pantalla.setup(width=800, height=600)
        self.pantalla.tracer(0)  # Desactiva animación automática

        # --- Tortuga principal (dibuja horca y cuerpo) ---
        self.lapiz = turtle.Turtle()
        self.lapiz.hideturtle()
        self.lapiz.speed(5)
        self.lapiz.pensize(4)
        self.lapiz.color("#cdd6f4")

        # --- Tortuga para texto en pantalla ---
        self.escritor = turtle.Turtle()
        self.escritor.hideturtle()
        self.escritor.penup()
        self.escritor.color("#cdd6f4")

        # --- Estado del juego ---
        self.palabras = [
            "python", "programacion", "universidad", "objeto",
            "clase", "metodo", "atributo", "herencia", "turtle",
            "algoritmo", "variable", "funcion", "modulo", "bucle"
        ]
        self.palabra_secreta = ""       # Se asigna al iniciar juego
        self.letras_adivinadas = []     # Letras correctas ingresadas
        self.letras_falladas = []       # Letras incorrectas ingresadas
        self.max_intentos = 6           # Cabeza, torso, 2 brazos, 2 piernas
        self.intentos_restantes = self.max_intentos

        # Actualiza la pantalla una vez configurado todo
        self.pantalla.update()


# -------------------------------------------------------
if __name__ == "__main__":
    juego = JuegoAhorcado()
    turtle.done()