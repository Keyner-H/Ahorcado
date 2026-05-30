# ahorcado.py
import turtle
import random


class JuegoAhorcado:
    """
    Juego del Ahorcado implementado con Programación Orientada a Objetos
    usando únicamente la librería turtle de Python.
    """

    def __init__(self):
        # --- Configuración de la ventana ---
        self.pantalla = turtle.Screen()
        self.pantalla.title("El Ahorcado - POO con Turtle")
        self.pantalla.bgcolor("#1e1e2e")
        self.pantalla.setup(width=800, height=600)
        self.pantalla.tracer(0)

        # --- Tortuga principal (dibuja horca y cuerpo) ---
        self.lapiz = turtle.Turtle()
        self.lapiz.hideturtle()
        self.lapiz.speed(5)
        self.lapiz.pensize(4)
        self.lapiz.color("#cdd6f4")

        # --- Tortuga exclusiva para texto ---
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
        self.palabra_secreta    = ""
        self.letras_adivinadas  = []
        self.letras_falladas    = []
        self.max_intentos       = 6
        self.intentos_restantes = self.max_intentos

        self.pantalla.update()

    # ----------------------------------------------------------
    # PARTE 2: DIBUJO DE LA HORCA
    # ----------------------------------------------------------

    def dibujar_horca(self):
        """Dibuja la estructura completa de la horca con coordenadas fijas."""
        self.lapiz.penup()
        self.lapiz.color("#f38ba8")
        self.lapiz.pensize(5)

        # 1) BASE horizontal: (-100, -100) → (100, -100)
        self.lapiz.goto(-100, -100)
        self.lapiz.pendown()
        self.lapiz.goto(100, -100)

        # 2) POSTE VERTICAL: (-50, -100) → (-50, 150)
        self.lapiz.penup()
        self.lapiz.goto(-50, -100)
        self.lapiz.pendown()
        self.lapiz.goto(-50, 150)

        # 3) TECHO SUPERIOR: (-50, 150) → (50, 150)
        self.lapiz.penup()
        self.lapiz.goto(-50, 150)
        self.lapiz.pendown()
        self.lapiz.goto(50, 150)

        # 4) CUERDA: (50, 150) → (50, 110)
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
        """Círculo radio=20 en (50,70); tope toca exactamente Y=110."""
        self.lapiz.color("#a6e3a1")
        self.lapiz.pensize(3)
        self.lapiz.penup()
        self.lapiz.goto(50, 70)
        self.lapiz.setheading(0)   # Apunta al este → el círculo sube
        self.lapiz.pendown()
        self.lapiz.circle(20)
        self.lapiz.penup()
        self.pantalla.update()

    def dibujar_torso(self):
        """Cuerpo vertical de (50, 70) a (50, -10)."""
        self.lapiz.color("#89b4fa")
        self.lapiz.pensize(4)
        self.lapiz.penup()
        self.lapiz.goto(50, 70)
        self.lapiz.pendown()
        self.lapiz.goto(50, -10)
        self.lapiz.penup()
        self.pantalla.update()

    def dibujar_brazo_izquierdo(self):
        """Brazo izquierdo de (50, 40) a (15, 10)."""
        self.lapiz.color("#fab387")
        self.lapiz.pensize(3)
        self.lapiz.penup()
        self.lapiz.goto(50, 40)
        self.lapiz.pendown()
        self.lapiz.goto(15, 10)
        self.lapiz.penup()
        self.pantalla.update()

    def dibujar_brazo_derecho(self):
        """Brazo derecho de (50, 40) a (85, 10)."""
        self.lapiz.color("#fab387")
        self.lapiz.pensize(3)
        self.lapiz.penup()
        self.lapiz.goto(50, 40)
        self.lapiz.pendown()
        self.lapiz.goto(85, 10)
        self.lapiz.penup()
        self.pantalla.update()

    def dibujar_pierna_izquierda(self):
        """Pierna izquierda de (50, -10) a (15, -60)."""
        self.lapiz.color("#cba6f7")
        self.lapiz.pensize(3)
        self.lapiz.penup()
        self.lapiz.goto(50, -10)
        self.lapiz.pendown()
        self.lapiz.goto(15, -60)
        self.lapiz.penup()
        self.pantalla.update()

    def dibujar_pierna_derecha(self):
        """Pierna derecha de (50, -10) a (85, -60)."""
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
        Despachador: llama al método correcto según el número de error (1-6).
        Orden: cabeza → torso → brazo izq → brazo der → pierna izq → pierna der.
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

    # ----------------------------------------------------------
    # PARTE 4: MÉTODOS DE TEXTO Y LÓGICA DEL JUEGO
    # ----------------------------------------------------------

    def mostrar_titulo(self):
        """Dibuja el título del juego en la parte superior de la pantalla."""
        self.escritor.penup()
        self.escritor.goto(0, 230)
        self.escritor.color("#cba6f7")
        self.escritor.write(
            "EL  AHORCADO",
            align="center",
            font=("Courier", 22, "bold")
        )

    def mostrar_palabra(self):
        """
        Muestra la palabra con letras adivinadas y guiones bajos
        para las letras aún ocultas.
        """
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
        """
        Panel derecho: muestra intentos restantes y letras falladas.
        Posicionado en X=180 para no solaparse con la horca (X=-50..100).
        """
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
        if self.letras_falladas:
            texto_falladas = "Falladas: " + "  ".join(self.letras_falladas).upper()
        else:
            texto_falladas = "Falladas: —"
        self.escritor.write(
            texto_falladas,
            align="left",
            font=("Courier", 12, "normal")
        )

    def limpiar_info(self):
        """
        Borra todo el texto (self.escritor) y lo redibuja actualizado.
        La horca y el cuerpo (dibujados por self.lapiz) NO se ven afectados.
        """
        self.escritor.clear()
        self.mostrar_titulo()
        self.mostrar_palabra()
        self.mostrar_panel_info()
        self.pantalla.update()

    def verificar_victoria(self):
        """Retorna True si todas las letras de la palabra fueron adivinadas."""
        return all(letra in self.letras_adivinadas for letra in self.palabra_secreta)

    def mostrar_resultado(self, gano: bool):
        """
        Escribe el mensaje final sobre la pantalla y abre un textinput
        informativo que actúa como diálogo de cierre.
        """
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
            self.pantalla.textinput(
                "GANASTE",
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
            self.pantalla.textinput(
                "GAME OVER",
                f"La palabra era: '{self.palabra_secreta.upper()}'\n"
                "Presiona OK para salir."
            )

    def jugar(self):
        """
        Método principal del juego. Flujo completo:
          1. Selecciona palabra aleatoria y resetea el estado.
          2. Dibuja la horca y el panel inicial.
          3. Bucle principal: pide letras con textinput.
          4. Valida entrada (longitud, alfabética, no repetida).
          5. Actualiza adivinadas/falladas y dibuja parte del cuerpo si falla.
          6. Refresca el panel de texto.
          7. Comprueba victoria o derrota y muestra el resultado final.
        """
        # 1. Inicialización
        self.palabra_secreta    = random.choice(self.palabras)
        self.letras_adivinadas  = []
        self.letras_falladas    = []
        self.intentos_restantes = self.max_intentos

        # 2. Escena inicial
        self.dibujar_horca()
        self.mostrar_titulo()
        self.mostrar_palabra()
        self.mostrar_panel_info()
        self.pantalla.update()

        # 3. Bucle principal
        while True:

            # Solicita letra
            entrada = self.pantalla.textinput(
                "El Ahorcado",
                f"Intentos restantes: {self.intentos_restantes}  |  "
                f"Falladas: {', '.join(self.letras_falladas).upper() or 'ninguna'}\n"
                "Escribe una letra:"
            )

            # Jugador cerró el diálogo
            if entrada is None:
                break

            letra = entrada.strip().lower()

            # Validación 1: exactamente una letra del alfabeto
            if len(letra) != 1 or not letra.isalpha():
                self.pantalla.textinput(
                    "Entrada inválida",
                    "Debes ingresar exactamente UNA letra del alfabeto.\n"
                    "Presiona OK e inténtalo de nuevo."
                )
                continue

            # Validación 2: letra no repetida
            if letra in self.letras_adivinadas or letra in self.letras_falladas:
                self.pantalla.textinput(
                    "Letra repetida",
                    f"La letra '{letra.upper()}' ya fue ingresada antes.\n"
                    "Presiona OK e intenta con otra letra."
                )
                continue

            # Procesa la letra
            if letra in self.palabra_secreta:
                self.letras_adivinadas.append(letra)
            else:
                self.letras_falladas.append(letra)
                self.intentos_restantes -= 1
                errores_acumulados = self.max_intentos - self.intentos_restantes
                self.dibujar_parte_cuerpo(errores_acumulados)

            # Refresca panel de texto
            self.limpiar_info()

            # Comprueba victoria
            if self.verificar_victoria():
                self.mostrar_resultado(gano=True)
                break

            # Comprueba derrota
            if self.intentos_restantes == 0:
                self.mostrar_resultado(gano=False)
                break


# -------------------------------------------------------
if __name__ == "__main__":
    juego = JuegoAhorcado()
    juego.jugar()
    turtle.done()