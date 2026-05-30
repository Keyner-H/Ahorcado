# ahorcado.py
import turtle
import random
import urllib.request
import json
import unicodedata


class JuegoAhorcado:
    """
    Juego del Ahorcado - POO con Turtle.
    Palabras reales obtenidas desde una API pública de español.
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
        self.lapiz.speed(0)
        self.lapiz.pensize(4)
        self.lapiz.color("#cdd6f4")

        # --- Tortuga exclusiva para texto ---
        self.escritor = turtle.Turtle()
        self.escritor.hideturtle()
        self.escritor.penup()
        self.escritor.color("#cdd6f4")

        # --- Fallback sin internet ---
        self._emergencia = [
            "programar", "computadora", "teclado", "algoritmo",
            "software", "internet", "variable", "funcion",
            "monitor", "impresora", "servidor", "compilador"
        ]

        # --- Estado del juego ---
        self.palabra_secreta    = ""
        self.letras_adivinadas  = []
        self.letras_falladas    = []
        self.max_intentos       = 6
        self.intentos_restantes = self.max_intentos

        self.pantalla.update()

    # ----------------------------------------------------------
    # UTILIDADES DE VENTANA Y TEXTO
    # ----------------------------------------------------------

    def _levantar_ventana(self):
        """
        Trae la ventana al frente antes de cada textinput.
        Evita que el diálogo quede oculto detrás de otras ventanas.
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
    # OBTENCIÓN DE PALABRA ALEATORIA REAL DESDE API
    # ----------------------------------------------------------

    def _normalizar_palabra(self, texto):
        """
        Elimina tildes y convierte a minúsculas.
        Ejemplo: 'Árbol' → 'arbol' | 'corazón' → 'corazon'
        Así el jugador solo necesita escribir letras simples.
        """
        texto       = texto.lower().strip()
        normalizado = unicodedata.normalize("NFD", texto)
        return "".join(c for c in normalizado if unicodedata.category(c) != "Mn")

    def _obtener_palabra_aleatoria(self):
        """
        Consulta la API pública de palabras en español.
        Pide 10 palabras a la vez para tener opciones de filtrado.
        Si no hay internet, usa la lista de emergencia automáticamente.
        """
        # Mensaje de carga mientras espera la API
        self.escritor.penup()
        self.escritor.goto(0, 0)
        self.escritor.color("#f9e2af")
        self.escritor.write(
            "Buscando palabra...",
            align="center",
            font=("Courier", 16, "italic")
        )
        self.pantalla.update()

        try:
            url = "https://random-word-api.vercel.app/api?words=10&lang=es"
            req = urllib.request.Request(
                url, headers={"User-Agent": "Mozilla/5.0"}
            )
            with urllib.request.urlopen(req, timeout=6) as respuesta:
                datos = json.loads(respuesta.read().decode("utf-8"))
                for palabra in datos:
                    limpia = self._normalizar_palabra(palabra)
                    # Solo letras a-z, entre 4 y 12 caracteres
                    if limpia.isalpha() and 4 <= len(limpia) <= 12:
                        self.escritor.clear()
                        return limpia
        except Exception:
            pass  # Sin internet → cae al fallback silenciosamente

        self.escritor.clear()
        return self._normalizar_palabra(random.choice(self._emergencia))

    # ----------------------------------------------------------
    # DIBUJO DE LA HORCA
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
    # PARTES DEL CUERPO
    # ----------------------------------------------------------

    def dibujar_cabeza(self):
        """Círculo radio=20 en (50,70); tope toca exactamente Y=110."""
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
        Despachador: dibuja la parte del cuerpo según el número de error (1-6).
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
    # TEXTO Y PANEL DE INFORMACIÓN
    # ----------------------------------------------------------

    def mostrar_titulo(self):
        """Dibuja el título del juego en la parte superior."""
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
        Muestra la palabra con letras adivinadas visibles
        y guiones bajos para las letras aún ocultas.
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
        """Panel derecho: intentos restantes y letras falladas."""
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
        self.escritor.write(
            texto,
            align="left",
            font=("Courier", 12, "normal")
        )

    def limpiar_info(self):
        """Borra solo el texto (self.escritor) y lo redibuja actualizado."""
        self.escritor.clear()
        self.mostrar_titulo()
        self.mostrar_palabra()
        self.mostrar_panel_info()
        self.pantalla.update()

    def verificar_victoria(self):
        """Retorna True si todas las letras fueron adivinadas."""
        return all(letra in self.letras_adivinadas for letra in self.palabra_secreta)

    def mostrar_resultado(self, gano: bool):
        """Escribe el mensaje final y abre el diálogo de cierre."""
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
        """
        Método principal del juego. Flujo completo:
          1. Obtiene una palabra real aleatoria desde la API.
          2. Dibuja la horca y el panel inicial.
          3. Bucle: pide letras, valida, actualiza estado y dibuja cuerpo.
          4. Comprueba victoria o derrota en cada turno.
        """
        # 1. Obtiene palabra real desde la API
        self.palabra_secreta    = self._obtener_palabra_aleatoria()
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

            self._levantar_ventana()
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
                self._levantar_ventana()
                self.pantalla.textinput(
                    "Entrada inválida",
                    "Debes ingresar UNA sola letra del alfabeto.\n"
                    "Presiona OK e inténtalo de nuevo."
                )
                continue

            # Normaliza por si el jugador escribe con tilde (é → e)
            letra = self._normalizar_palabra(letra)

            # Validación 2: letra no repetida
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

            # Refresca el panel de texto
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