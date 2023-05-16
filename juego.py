import dado


class Juego:
    __jugador1 = ""
    __jugador2 = ""
    __jugador3 = ""
    __lanzamientos = 0

    def __init__(self, jugador1, jugador2, jugador3, caras1, caras2, caras3, lanzamientos, intermedios):
        self.set_jugador1(jugador1)
        self.set_jugador2(jugador2)
        self.set_jugador3(jugador3)
        self.set_lanzamientos(lanzamientos)
        self.dado1 = dado.Dado(caras1)
        self.dado2 = dado.Dado(caras2)
        self.dado3 = dado.Dado(caras3)
        # Me guardo en un atributo booelano si necesito o no ver los datos intermedios
        self.__intermedios = (intermedios in ("S", "s"))
        self.resultadoJugador1 = 0
        self.resultadoJugador2 = 0
        self.resultadoJugador3 = 0

    def set_jugador1(self, fjugador1):
        if len(fjugador1) > 20:
            raise Exception("La longitud del nombre del jugador 1 no puede ser mayor de 20")
        else:
            self.__jugador1 = fjugador1

    def set_jugador2(self, fjugador2):
        if len(fjugador2) > 20:
            raise Exception("La longitud del nombre del jugador 2 no puede ser mayor de 20")
        else:
            self.__jugador2 = fjugador2

    def set_jugador2(self, fjugador2):
        if len(fjugador2) > 20:
            raise Exception("La longitud del nombre del jugador 2 no puede ser mayor de 20")
        else:
            self.__jugador2 = fjugador2

    def set_jugador3(self, fjugador3):
        if len(fjugador3) > 20:
            raise Exception("La longitud del nombre del jugador 2 no puede ser mayor de 20")
        else:
            self.__jugador3 = fjugador3

    def set_lanzamientos(self, flanzamientos):
        if not 2 < flanzamientos <= 1000:
            raise Exception("El número de lanzamientos debe de estar entre 2 y 1000")
        else:
            self.__lanzamientos = flanzamientos

    def jugar(self):
        for lanzamiento in range(self.__lanzamientos):
            # jugador1
            tirada1 = self.dado1.lanzar()
            tirada2 = self.dado2.lanzar()
            tirada3 = self.dado3.lanzar()
            self.resultadoJugador1 += (tirada1 + tirada2 + tirada3)

            if self.__intermedios:
                print(f"Lanzamiento {lanzamiento + 1}:")
                print(
                    f"{self.__jugador1}: {tirada1} {tirada2} {tirada3} ({(tirada1 + tirada2 + tirada3)})")

            # jugador2
            tirada1 = self.dado1.lanzar()
            tirada2 = self.dado2.lanzar()
            tirada3 = self.dado3.lanzar()
            self.resultadoJugador2 += (tirada1 + tirada2 + tirada3)

            if self.__intermedios:
                print(
                    f"{self.__jugador2}: {tirada1} {tirada2} {tirada3} ({(tirada1 + tirada2 + tirada3)})")


                # jugador3
                tirada1 = self.dado1.lanzar()
                tirada2 = self.dado2.lanzar()
                tirada3 = self.dado3.lanzar()
                self.resultadoJugador3 += (tirada1 + tirada2 + tirada3)

                if self.__intermedios:
                    print(
                        f"{self.__jugador3}: {tirada1} {tirada2} {tirada3} ({(tirada1 + tirada2 + tirada3)})")
                    print("")

    def mostrarPuntuaciones(self):
        print("Resultados:")
        print(f"Jugador 1: {self.__jugador1}")
        print(f"Jugador 2: {self.__jugador2}")
        print(f"Numero de lanzamientos: {self.__lanzamientos}")
        print(f"Dados: {self.dado1.getCaras()},{self.dado2.getCaras()} y {self.dado3.getCaras()} ")
        print(f"Puntos jugador 1: {self.resultadoJugador1}")
        print(f"Puntos jugador 2: {self.resultadoJugador2}")
        if self.resultadoJugador1 > self.resultadoJugador2:
            print(f"El GANADOR es {self.__jugador1} con {self.resultadoJugador1} puntos")
        elif self.resultadoJugador1 == self.resultadoJugador2:
            print("Ha habido un EMPATE")
        else:
            print(f"El GANADOR es {self.__jugador2} con {self.resultadoJugador2} puntos")
        if self.resultadoJugador1 > self.resultadoJugador2 > self.resultadoJugador1:
            print("El mundo se acaba")
