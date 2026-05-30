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
        """Dibuja la estructura completa de la horca."""
        self.lapiz.penup()
        self.lapiz.color("#f38ba8")
        self.lapiz.pensize(5)

        # 1) BASE horizontal
        self.lapiz.goto(-100, -100)
        self.lapiz.pendown()
        self.lapiz.goto(100, -100)

        # 2) POSTE VERTICAL
        self.lapiz.penup()
        self.lapiz.goto(-50, -100)
        self.lapiz.pendown()
        self.lapiz.goto(-50, 150)

        # 3) TECHO SUPERIOR
        self.lapiz.penup()
        self.lapiz.goto(-50, 150)
        self.lapiz.pendown()
        self.lapiz.goto(50, 150)

        # 4) CUERDA
        self.lapiz.penup()
        self.lapiz.goto(50, 150)
        self.lapiz.pendown()
        self.lapiz.goto(50, 110)

        self.lapiz.penup()
        self.pantalla.update()

    # ----------------------------------------------------------
    # PARTE 3: PARTES DEL CUERPO (cuelgan en X=50)
    # ----------------------------------------------------------

    def dibujar_cabeza(self):
        """
        Dibuja un círculo de radio 20.
        Tortuga en (50, 70) mirando al este → centro en (50, 90)
        → parte superior toca exactamente Y=110 (fin de la cuerda).
        """
        self.lapiz.color("#a6e3a1")   # Verde suave
        self.lapiz.pensize(3)
        self.lapiz.penup()
        self.lapiz.goto(50, 70)
        self.lapiz.setheading(0)      # Apunta al este (derecha)
        self.lapiz.pendown()
        self.lapiz.circle(20)         # Centro=(50,90), tope=Y110 ✓
        self.lapiz.penup()
        self.pantalla.update()

    def dibujar_torso(self):
        """
        Dibuja el cuerpo desde (50, 70) hasta (50, -10).
        Baja verticalmente en el eje X=50.
        """
        self.lapiz.color("#89b4fa")   # Azul suave
        self.lapiz.pensize(4)
        self.lapiz.penup()
        self.lapiz.goto(50, 70)
        self.lapiz.pendown()
        self.lapiz.goto(50, -10)
        self.lapiz.penup()
        self.pantalla.update()

    def dibujar_brazo_izquierdo(self):
        """
        Brazo izquierdo: parte del cuerpo en (50, 40)
        hacia la izquierda-abajo hasta (15, 10).
        """
        self.lapiz.color("#fab387")   # Naranja suave
        self.lapiz.pensize(3)
        self.lapiz.penup()
        self.lapiz.goto(50, 40)
        self.lapiz.pendown()
        self.lapiz.goto(15, 10)
        self.lapiz.penup()
        self.pantalla.update()

    def dibujar_brazo_derecho(self):
        """
        Brazo derecho: parte del cuerpo en (50, 40)
        hacia la derecha-abajo hasta (85, 10).
        """
        self.lapiz.color("#fab387")
        self.lapiz.pensize(3)
        self.lapiz.penup()
        self.lapiz.goto(50, 40)
        self.lapiz.pendown()
        self.lapiz.goto(85, 10)
        self.lapiz.penup()
        self.pantalla.update()

    def dibujar_pierna_izquierda(self):
        """
        Pierna izquierda: sale de la base del torso (50, -10)
        hacia la izquierda-abajo hasta (15, -60).
        """
        self.lapiz.color("#cba6f7")   # Violeta suave
        self.lapiz.pensize(3)
        self.lapiz.penup()
        self.lapiz.goto(50, -10)
        self.lapiz.pendown()
        self.lapiz.goto(15, -60)
        self.lapiz.penup()
        self.pantalla.update()

    def dibujar_pierna_derecha(self):
        """
        Pierna derecha: sale de la base del torso (50, -10)
        hacia la derecha-abajo hasta (85, -60).
        """
        self.lapiz.color("#cba6f7")
        self.lapiz.pensize(3)
        self.lapiz.penup()
        self.lapiz.goto(50, -10)
        self.lapiz.pendown()
        self.lapiz.goto(85, -60)
        self.lapiz.penup()
        self.pantalla.update()

    def dibujar_parte_cuerpo(self, numero_error):
        """
        Despacha la parte del cuerpo según el número de error (1-6).
        Orden: cabeza → torso → brazo izq → brazo der
               → pierna izq → pierna der.
        """
        partes = {
            1: self.dibujar_cabeza,
            2: self.dibujar_torso,
            3: self.dibujar_brazo_izquierdo,
            4: self.dibujar_brazo_derecho,
            5: self.dibujar_pierna_izquierda,
            6: self.dibujar_pierna_derecha,
        }
        if numero_error in partes:
            partes[numero_error]()


# -------------------------------------------------------
if __name__ == "__main__":
    juego = JuegoAhorcado()
    juego.dibujar_horca()

    # Prueba visual: dibuja el muñeco completo parte a parte
    for error in range(1, 7):
        juego.dibujar_parte_cuerpo(error)

    turtle.done()