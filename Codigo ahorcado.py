# ahorcado.py
import turtle
import random


class JuegoAhorcado:
    """
    Juego del Ahorcado - POO con Turtle.
    Corrección: _levantar_ventana() fuerza el foco antes de cada textinput.
    """

    def __init__(self):
        self.pantalla = turtle.Screen()
        self.pantalla.title("El Ahorcado - POO con Turtle")
        self.pantalla.bgcolor("#1e1e2e")
        self.pantalla.setup(width=800, height=600)
        self.pantalla.tracer(0)

        self.lapiz = turtle.Turtle()
        self.lapiz.hideturtle()
        self.lapiz.speed(0)
        self.lapiz.pensize(4)
        self.lapiz.color("#cdd6f4")

        self.escritor = turtle.Turtle()
        self.escritor.hideturtle()
        self.escritor.penup()
        self.escritor.color("#cdd6f4")

        self.palabras = [
            "python", "programacion", "universidad", "objeto",
            "clase", "metodo", "atributo", "herencia", "turtle",
            "algoritmo", "variable", "funcion", "modulo", "bucle"
        ]
        self.palabra_secreta    = ""
        self.letras_adivinadas  = []
        self.letras_falladas    = []
        self.max_intentos       = 6
        self.intentos_restantes = self.max_intentos

        self.pantalla.update()

    # ----------------------------------------------------------
    # CORRECCIÓN CLAVE: forzar foco de ventana antes de textinput
    # ----------------------------------------------------------

    def _levantar_ventana(self):
        """
        Usa tkinter (base de turtle) para traer la ventana al frente
        antes de mostrar cualquier textinput. Sin esto, el diálogo
        queda oculto detrás y parece que el juego no responde.
        """
        try:
            canvas = self.pantalla.getcanvas()
            root   = canvas.winfo_toplevel()
            root.lift()
            root.attributes("-topmost", True)
            root.after(150, lambda: root.attributes("-topmost", False))
            root.focus_force()
            self.pantalla.update()
        except Exception:
            pass

    # ----------------------------------------------------------
    # DIBUJO DE LA HORCA
    # ----------------------------------------------------------

    def dibujar_horca(self):
        """Dibuja la estructura completa de la horca con coordenadas fijas."""
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
    # PARTES DEL CUERPO
    # ----------------------------------------------------------

    def dibujar_cabeza(self):
        self.lapiz.color("#a6e3a1")
        self.lapiz.pensize(3)
        self.lapiz.penup()
        self.lapiz.goto(50, 70)
        self.lapiz.setheading(0)
        self.lapiz.pendown()
        self.lapiz.circle(20)
        self.lapiz.penup()
        self.pantalla.update()

    def dibujar_torso(self):
        self.lapiz.color("#89b4fa")
        self.lapiz.pensize(4)
        self.lapiz.penup()
        self.lapiz.goto(50, 70)
        self.lapiz.pendown()
        self.lapiz.goto(50, -10)
        self.lapiz.penup()
        self.pantalla.update()

    def dibujar_brazo_izquierdo(self):
        self.lapiz.color("#fab387")
        self.lapiz.pensize(3)
        self.lapiz.penup()
        self.lapiz.goto(50, 40)
        self.lapiz.pendown()
        self.lapiz.goto(15, 10)
        self.lapiz.penup()
        self.pantalla.update()

    def dibujar_brazo_derecho(self):
        self.lapiz.color("#fab387")
        self.lapiz.pensize(3)
        self.lapiz.penup()
        self.lapiz.goto(50, 40)
        self.lapiz.pendown()
        self.lapiz.goto(85, 10)
        self.lapiz.penup()
        self.pantalla.update()

    def dibujar_pierna_izquierda(self):
        self.lapiz.color("#cba6f7")
        self.lapiz.pensize(3)
        self.lapiz.penup()
        self.lapiz.goto(50, -10)
        self.lapiz.pendown()
        self.lapiz.goto(15, -60)
        self.lapiz.penup()
        self.pantalla.update()

    def dibujar_pierna_derecha(self):
        self.lapiz.color("#cba6f7")
        self.lapiz.pensize(3)
        self.lapiz.penup()
        self.lapiz.goto(50, -10)
        self.lapiz.pendown()
        self.lapiz.goto(85, -60)
        self.lapiz.penup()
        self.pantalla.update()

    def dibujar_parte_cuerpo(self, numero_error):
        """Despachador: dibuja la parte correspondiente al error N."""
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

    # ----------------------------------------------------------
    # TEXTO Y PANEL DE INFORMACIÓN
    # ----------------------------------------------------------

    def mostrar_titulo(self):
        self.escritor.penup()
        self.escritor.goto(0, 230)
        self.escritor.color("#cba6f7")
        self.escritor.write(
            "EL  AHORCADO",
            align="center",
            font=("Courier", 22, "bold")
        )

    def mostrar_palabra(self):
        display = "  ".join(
            letra.upper() if letra in self.letras_adivinadas else "_"
            for letra in self.palabra_secreta
        )
        self.escritor.penup()
        self.escritor.goto(0, -185)
        self.escritor.color("#a6e3a1")
        self.escritor.write(
            display,
            align="center",
            font=("Courier", 18, "bold")
        )

    def mostrar_panel_info(self):
        # Intentos restantes
        self.escritor.penup()
        self.escritor.goto(180, 80)
        self.escritor.color("#f9e2af")
        self.escritor.write(
            f"Intentos: {self.intentos_restantes} / {self.max_intentos}",
            align="left",
            font=("Courier", 13, "bold")
        )
        # Letras falladas
        self.escritor.penup()
        self.escritor.goto(180, 40)
        self.escritor.color("#f38ba8")
        texto = (
            "Falladas: " + "  ".join(self.letras_falladas).upper()
            if self.letras_falladas else "Falladas: —"
        )
        self.escritor.write(texto, align="left", font=("Courier", 12, "normal"))

    def limpiar_info(self):
        """Borra solo el texto (escritor) y lo redibuja actualizado."""
        self.escritor.clear()
        self.mostrar_titulo()
        self.mostrar_palabra()
        self.mostrar_panel_info()
        self.pantalla.update()

    def verificar_victoria(self):
        return all(letra in self.letras_adivinadas for letra in self.palabra_secreta)

    def mostrar_resultado(self, gano: bool):
        self.escritor.penup()
        self.escritor.goto(0, 175)
        if gano:
            self.escritor.color("#a6e3a1")
            self.escritor.write(
                "¡¡ G A N A S T E !!",
                align="center",
                font=("Courier", 20, "bold")
            )
            self.pantalla.update()
            self._levantar_ventana()
            self.pantalla.textinput(
                "GANASTE 🎉",
                f"¡Felicitaciones! La palabra era: '{self.palabra_secreta.upper()}'\n"
                "Presiona OK para salir."
            )
        else:
            self.escritor.color("#f38ba8")
            self.escritor.write(
                "¡ P E R D I S T E !",
                align="center",
                font=("Courier", 20, "bold")
            )
            self.pantalla.update()
            self._levantar_ventana()
            self.pantalla.textinput(
                "GAME OVER",
                f"La palabra era: '{self.palabra_secreta.upper()}'\n"
                "Presiona OK para salir."
            )

    # ----------------------------------------------------------
    # BUCLE PRINCIPAL
    # ----------------------------------------------------------

    def jugar(self):
        """Método principal: selecciona palabra y gestiona el bucle del juego."""
        self.palabra_secreta    = random.choice(self.palabras)
        self.letras_adivinadas  = []
        self.letras_falladas    = []
        self.intentos_restantes = self.max_intentos

        self.dibujar_horca()
        self.mostrar_titulo()
        self.mostrar_palabra()
        self.mostrar_panel_info()
        self.pantalla.update()

        while True:
            # ← CORRECCIÓN: levanta la ventana antes de pedir input
            self._levantar_ventana()

            entrada = self.pantalla.textinput(
                "El Ahorcado",
                f"Intentos restantes: {self.intentos_restantes}  |  "
                f"Falladas: {', '.join(self.letras_falladas).upper() or 'ninguna'}\n"
                "Escribe una letra:"
            )

            if entrada is None:          # Jugador cerró el diálogo
                break

            letra = entrada.strip().lower()

            # Validación 1: exactamente una letra
            if len(letra) != 1 or not letra.isalpha():
                self._levantar_ventana()
                self.pantalla.textinput(
                    "Entrada inválida",
                    "Debes ingresar UNA sola letra del alfabeto.\n"
                    "Presiona OK e inténtalo de nuevo."
                )
                continue

            # Validación 2: no repetida
            if letra in self.letras_adivinadas or letra in self.letras_falladas:
                self._levantar_ventana()
                self.pantalla.textinput(
                    "Letra repetida",
                    f"La letra '{letra.upper()}' ya fue ingresada.\n"
                    "Presiona OK e intenta con otra."
                )
                continue

            # Procesa la letra
            if letra in self.palabra_secreta:
                self.letras_adivinadas.append(letra)
            else:
                self.letras_falladas.append(letra)
                self.intentos_restantes -= 1
                errores = self.max_intentos - self.intentos_restantes
                self.dibujar_parte_cuerpo(errores)

            self.limpiar_info()

            if self.verificar_victoria():
                self.mostrar_resultado(gano=True)
                break

            if self.intentos_restantes == 0:
                self.mostrar_resultado(gano=False)
                break


# -------------------------------------------------------
if __name__ == "__main__":
    juego = JuegoAhorcado()
    juego.jugar()
    turtle.done()