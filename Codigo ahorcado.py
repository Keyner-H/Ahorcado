# ahorcado.py
import turtle
import random

class JuegoAhorcado:

    def __init__(self):
        # --- Configuración de la ventana ---
        self.pantalla = turtle.Screen()
        self.pantalla.title("El Ahorcado - POO con Turtle")
        self.pantalla.bgcolor("#1e1e2e")
        self.pantalla.setup(width=800, height=600)
        self.pantalla.tracer(0)

        # --- Tortuga principal ---
        self.lapiz = turtle.Turtle()
        self.lapiz.hideturtle()
        self.lapiz.speed(5)
        self.lapiz.pensize(4)
        self.lapiz.color("#cdd6f4")

        # --- Tortuga para texto ---
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
        self.palabra_secreta = ""
        self.letras_adivinadas = []
        self.letras_falladas = []
        self.max_intentos = 6
        self.intentos_restantes = self.max_intentos

        self.pantalla.update()

    # ----------------------------------------------------------
    # PARTE 2: DIBUJO DE LA HORCA
    # ----------------------------------------------------------

    def dibujar_horca(self):
        """
        Dibuja la estructura completa de la horca usando
        coordenadas absolutas fijas con goto().
        Partes: base, poste vertical, techo superior y cuerda.
        """
        self.lapiz.penup()
        self.lapiz.color("#f38ba8")   # Rojo suave para la horca
        self.lapiz.pensize(5)

        # 1) BASE horizontal: de (-100, -100) a (100, -100)
        self.lapiz.goto(-100, -100)
        self.lapiz.pendown()
        self.lapiz.goto(100, -100)

        # 2) POSTE VERTICAL: sube desde (-50, -100) hasta (-50, 150)
        self.lapiz.penup()
        self.lapiz.goto(-50, -100)
        self.lapiz.pendown()
        self.lapiz.goto(-50, 150)

        # 3) TECHO SUPERIOR: va desde (-50, 150) hasta (50, 150)
        self.lapiz.penup()
        self.lapiz.goto(-50, 150)
        self.lapiz.pendown()
        self.lapiz.goto(50, 150)

        # 4) CUERDA: baja desde (50, 150) hasta (50, 110)
        self.lapiz.penup()
        self.lapiz.goto(50, 150)
        self.lapiz.pendown()
        self.lapiz.goto(50, 110)

        self.lapiz.penup()
        self.pantalla.update()


# -------------------------------------------------------
if __name__ == "__main__":
    juego = JuegoAhorcado()
    juego.dibujar_horca()   # ← Prueba visual del commit
    turtle.done()