import random
import csv
from datetime import date


class PlayColombia:
    def __init__(self):
        self.__categoria = 1
        self.__nombre = "Jugador"
        self.__puntaje = 0
        self.__preguntas = []

    def nuevoJugador(self, nombre):
        # Este metodo guarda el nombre del jugador, imprime las reglas del juego y los puntajes por ronda
        # Lanza la primera ronda del juego
        print("Nombre de jugador guardado")
        self.__nombre = nombre
        print("Bienvenidx ", self.__nombre)

        print(
            "Jugaremos 5 rondas, cada ronda incrementa la complejidad\nLos puntos se asignaran de la siguiente manera:")
        print(
            "    Ronda 1 -> 10 puntos\n    Ronda 2 -> 20 puntos\n    Ronda 3 -> 30 puntos\n    Ronda 4 -> 40 puntos\n    Ronda 5 -> 100 puntos")
        self.leerArchivo()  # Carga las preguntas al juego
        self.jugarRonda()

    def leerArchivo(self):
        # Carga el archivo csv con las preguntas, cada 5 filas son una nueva categoría
        # Se convierte a diccionario y se adjuntana una lista para operarlo fácilmente

        with open('categorias.csv', encoding="utf8") as csvfile:
            for row in csv.DictReader(csvfile, delimiter=','):
                self.__preguntas.append(row)

    def puntosRonda(self):
        # Este metodo devuelve la cantidad de puntos a obtener segun la ronda que se este jugando
        if self.__categoria == 1:
            val = 10
        elif self.__categoria == 2:
            val = 20
        elif self.__categoria == 3:
            val = 30
        elif self.__categoria == 4:
            val = 40
        elif self.__categoria == 5:
            val = 100

        texto = "Por " + str(val) + " puntos"
        return texto

    def cargarPreguntas(self):
        # Carga las preguntas del archivo

        aleatorio = int(random.uniform(0, 5))  # Genera un numero aleatorio que se suma con el marcador para elegir la pregunta

        # El marcador varia en funcion de la categoría en la que este el jugador
        # se usa para moverse entre las lineas del archivo que contiene las preguntas
        marcador = 5 * (self.__categoria - 1)

        pregunta = self.__preguntas[aleatorio + marcador]['pregunta']
        opcion1 = self.__preguntas[aleatorio + marcador]['opcion1']
        opcion2 = self.__preguntas[aleatorio + marcador]['opcion2']
        opcion3 = self.__preguntas[aleatorio + marcador]['opcion3']
        opcion4 = self.__preguntas[aleatorio + marcador]['opcion4']
        mensaje = self.__preguntas[aleatorio + marcador]['mensaje']
        respuesta = self.__preguntas[aleatorio + marcador]['correcta']
        return pregunta, opcion1, opcion2, opcion3, opcion4, respuesta, mensaje

    def pasarNivel(self):
        # Incrementa el nivel o la ronda del juego, cuando este valor es 5 termina el juego
        if self.__categoria < 5:
            self.__categoria += 1
            self.jugarRonda()
        else:
            self.terminarJuego()

    def leerHistoricos(self):
        # Este método lee las puntuaciones historicas como diccionarios y los adjunta a una lista
        historicos = []
        with open('historicos.csv', encoding="utf8") as csvfile:
            for row in csv.DictReader(csvfile, delimiter=','):
                row['puntaje'] = int(row['puntaje'])
                historicos.append(row)

        return historicos

    def guardarHistorico(self):
        #Se cargan los datos del archivo csv
        historicos = self.leerHistoricos()
        # Se crea un diccionario con los datos del jugador actual y se suman a la lista que contiene a los historiocs
        jugadorAct = {"nombre": self.__nombre, "puntaje": int(self.__puntaje), "categoria": self.__categoria, "fecha": str(date.today())}
        historicos.append(jugadorAct)
        # Se ordenan los datos con base al puntaje antes de ser guardados
        historicos.sort(key=lambda p: p['puntaje'], reverse=True)

        with open('historicos.csv', 'w', newline='') as csvfile:
            cabezera = ["nombre", "puntaje", "categoria", "fecha"]
            writer = csv.DictWriter(csvfile, fieldnames=cabezera)

            writer.writeheader()
            for i in historicos:
                writer.writerow(i)

    def sumarPuntos(self):
        # Este método suma los puntos al acumulado del jugador en caso de qu ela respuesta sea la correcta
        if self.__categoria == 1:
            self.__puntaje += 10
        elif self.__categoria == 2:
            self.__puntaje += 20
        elif self.__categoria == 3:
            self.__puntaje += 30
        elif self.__categoria == 4:
            self.__puntaje += 40
        elif self.__categoria == 5:
            self.__puntaje += 100
        print("Puntos acumulados: ", self.__puntaje, "\n")

        self.pasarNivel()

    def validarResultados(self, respuesta, opcion, mensaje):
        if respuesta == opcion:
            print("---------Respuesta Correcta-----------")
            print(mensaje)
            self.sumarPuntos()
        else:
            print("x-x-x-x-x--Respuesta incorrectax--x-x-x-x\nJuego terminado")
            print("La respuesta correcta es: ", mensaje)
            print("Puntos acumulados: ", self.__puntaje, "\n")
            self.terminarJuego()

    def terminarJuego(self):
        # Guarda los datos del usuario y luego lee todos los datos historicos incluidos los del actual jugador
        self.guardarHistorico()
        print("Historicos")
        historicos = self.leerHistoricos()
        for i in historicos:
            print(".............................")
            for y in i:
                print(y, " -->", i[y])


    def lanzarJuego(self):
        # Lanza el juego con un mensaje de presentación
        # solicita el nombre del jugador y llama el metodos que configura el nombre del jugador

        print("Bienvenido a: ¿Quién es un buen Colombiano?\n\n")
        print("Este juego reta tus conocimientos de la cultura general colombiana")
        print("¿Estás listx para empezar? \n")

        nombreJugador = input("Por favor ingresa tu nombre: ")

        self.nuevoJugador(nombreJugador)

    def jugarRonda(self):
        # Se limita la cantidad de juegos a solo 5 rondas
        if self.__categoria <= 5:
            # Se cargan las preguntas y respuestas del archivo
            pregunta, opcion1, opcion2, opcion3, opcion4, respuesta, mensaje = self.cargarPreguntas()
            print("\n\nSi desea salir del juego responda Z\n")
            print("Ronda ", self.__categoria, "    -   ", self.puntosRonda())
            print("   * ", pregunta)
            print("   A. ", opcion1)
            print("   B. ", opcion2)
            print("   C. ", opcion3)
            print("   D. ", opcion4)

            controlador = True
            while controlador:
                opcionJugador = input("Ingresa la respuesta: ")
                if opcionJugador == "A" or opcionJugador == "B" or opcionJugador == "C" or opcionJugador == "D":
                    self.validarResultados(respuesta, opcionJugador, mensaje)
                    controlador = False
                elif opcionJugador == "Z":
                    print("Juego terminado")
                    print("puntos acumulados: ", self.__puntaje, "\n")
                    self.terminarJuego()
                    controlador = False
                else:
                    print("Ingresa una opción valida por favor\n\n")


juego1 = PlayColombia()
juego1.lanzarJuego()
