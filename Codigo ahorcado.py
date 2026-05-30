# ahorcado.py
import turtle
import random

class JuegoAhorcado:
    """Juego del Ahorcado con Programación Orientada a Objetos usando Turtle."""

    def __init__(self):
        # Configuración de la ventana principal
        self.pantalla = turtle.Screen()
        self.pantalla.title("El Ahorcado - POO con Turtle")
        self.pantalla.bgcolor("#1e1e2e")
        self.pantalla.setup(width=800, height=600)
        
        # Desactiva la animación automática para que el dibujo aparezca de golpe
        self.pantalla.tracer(0) 

        # Tortuga para dibujar la horca y el muñeco
        self.lapiz = turtle.Turtle()
        self.lapiz.hideturtle()
        self.lapiz.speed(0)
        self.lapiz.pensize(4)
        self.lapiz.color("#cdd6f4")

        # Tortuga exclusiva para los textos (permite borrar el texto sin borrar el dibujo)
        self.escritor = turtle.Turtle()
        self.escritor.hideturtle()
        self.escritor.penup()
        self.escritor.color("#cdd6f4")

        # Variables de estado del juego
        self.palabras = [
            "python", "programacion", "universidad", "objeto",
            "clase", "metodo", "atributo", "herencia", "turtle",
            "algoritmo", "variable", "funcion", "modulo", "bucle"
        ]
        self.palabra_secreta    = ""
        self.letras_adivinadas  = []
        self.letras_falladas    = []
        self.max_intentos       = 6 # Seis intentos por las 6 partes del cuerpo
        self.intentos_restantes = self.max_intentos

        self.pantalla.update()

    # ----------------------------------------------------------
    # Corrección para la ventana emergente
    # ----------------------------------------------------------
    def _levantar_ventana(self):
        """
        Fuerza a que la ventana de texto aparezca al frente. 
        En turtle a veces la ventana de textinput se queda escondida atrás.
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
    # Funciones de dibujo (usando coordenadas fijas)
    # ----------------------------------------------------------
    def dibujar_horca(self):
        """Dibuja la estructura base de la horca."""
        self.lapiz.penup()
        self.lapiz.color("#f38ba8")
        self.lapiz.pensize(5)

        # Base horizontal
        self.lapiz.goto(-100, -100)
        self.lapiz.pendown()
        self.lapiz.goto(100, -100)

        # Poste vertical
        self.lapiz.penup()
        self.lapiz.goto(-50, -100)
        self.lapiz.pendown()
        self.lapiz.goto(-50, 150)

        # Techo superior
        self.lapiz.penup()
        self.lapiz.goto(-50, 150)
        self.lapiz.pendown()
        self.lapiz.goto(50, 150)

        # Cuerda
        self.lapiz.penup()
        self.lapiz.goto(50, 150)
        self.lapiz.pendown()
        self.lapiz.goto(50, 110)

        self.lapiz.penup()
        self.pantalla.update()

    # --- Dibujo del muñeco (Empieza en X=50, bajo la cuerda) ---
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
        """Llama a la función de dibujo correspondiente según el número de errores."""
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
    # Interfaz de texto
    # ----------------------------------------------------------
    def mostrar_titulo(self):
        self.escritor.penup()
        self.escritor.goto(0, 230)
        self.escritor.color("#cba6f7")
        self.escritor.write("EL  AHORCADO", align="center", font=("Courier", 22, "bold"))

    def mostrar_palabra(self):
        # Construye el texto con las letras adivinadas o guiones bajos si falta adivinar
        display = "  ".join(
            letra.upper() if letra in self.letras_adivinadas else "_"
            for letra in self.palabra_secreta
        )
        self.escritor.penup()
        self.escritor.goto(0, -185)
        self.escritor.color("#a6e3a1")
        self.escritor.write(display, align="center", font=("Courier", 18, "bold"))

    def mostrar_panel_info(self):
        # Panel de intentos restantes
        self.escritor.penup()
        self.escritor.goto(180, 80)
        self.escritor.color("#f9e2af")
        self.escritor.write(
            f"Intentos: {self.intentos_restantes} / {self.max_intentos}",
            align="left", font=("Courier", 13, "bold")
        )
        
        # Panel de letras falladas
        self.escritor.penup()
        self.escritor.goto(180, 40)
        self.escritor.color("#f38ba8")
        texto = (
            "Falladas: " + "  ".join(self.letras_falladas).upper()
            if self.letras_falladas else "Falladas: —"
        )
        self.escritor.write(texto, align="left", font=("Courier", 12, "normal"))

    def limpiar_info(self):
        """Borra los textos anteriores y los redibuja con los datos actualizados."""
        self.escritor.clear()
        self.mostrar_titulo()
        self.mostrar_palabra()
        self.mostrar_panel_info()
        self.pantalla.update()

    # ----------------------------------------------------------
    # Lógica de fin de juego
    # ----------------------------------------------------------
    def verificar_victoria(self):
        return all(letra in self.letras_adivinadas for letra in self.palabra_secreta)

    def mostrar_resultado(self, gano: bool):
        self.escritor.penup()
        self.escritor.goto(0, 175)
        
        if gano:
            self.escritor.color("#a6e3a1")
            self.escritor.write("¡¡ G A N A S T E !!", align="center", font=("Courier", 20, "bold"))
            self.pantalla.update()
            self._levantar_ventana()
            self.pantalla.textinput(
                "GANASTE 🎉",
                f"¡Felicitaciones! La palabra era: '{self.palabra_secreta.upper()}'\n"
                "Presiona OK para salir."
            )
        else:
            self.escritor.color("#f38ba8")
            self.escritor.write("¡ P E R D I S T E !", align="center", font=("Courier", 20, "bold"))
            self.pantalla.update()
            self._levantar_ventana()
            self.pantalla.textinput(
                "GAME OVER",
                f"La palabra era: '{self.palabra_secreta.upper()}'\n"
                "Presiona OK para salir."
            )

    # ----------------------------------------------------------
    # Bucle principal del juego
    # ----------------------------------------------------------
    def jugar(self):
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
            self._levantar_ventana()

            entrada = self.pantalla.textinput(
                "El Ahorcado",
                f"Intentos restantes: {self.intentos_restantes}  |  "
                f"Falladas: {', '.join(self.letras_falladas).upper() or 'ninguna'}\n"
                "Escribe una letra:"
            )

            # Cierra el juego si el usuario presiona cancelar
            if entrada is None:          
                break

            letra = entrada.strip().lower()

            # Valida que sea solo una letra del abecedario
            if len(letra) != 1 or not letra.isalpha():
                self._levantar_ventana()
                self.pantalla.textinput(
                    "Entrada inválida",
                    "Debes ingresar UNA sola letra.\nPresiona OK e inténtalo de nuevo."
                )
                continue

            # Valida que la letra no se haya ingresado antes
            if letra in self.letras_adivinadas or letra in self.letras_falladas:
                self._levantar_ventana()
                self.pantalla.textinput(
                    "Letra repetida",
                    f"La letra '{letra.upper()}' ya fue ingresada.\nPresiona OK e intenta con otra."
                )
                continue

            # Procesamiento de la jugada
            if letra in self.palabra_secreta:
                self.letras_adivinadas.append(letra)
            else:
                self.letras_falladas.append(letra)
                self.intentos_restantes -= 1
                errores = self.max_intentos - self.intentos_restantes
                self.dibujar_parte_cuerpo(errores)

            self.limpiar_info()

            # Evalúa si se alcanzó la victoria o la derrota
            if self.verificar_victoria():
                self.mostrar_resultado(gano=True)
                break

            if self.intentos_restantes == 0:
                self.mostrar_resultado(gano=False)
                break


# Ejecución del programa
if __name__ == "__main__":
    juego = JuegoAhorcado()
    juego.jugar()
    turtle.done()