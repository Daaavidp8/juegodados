import dado


class Juego:
    """
    Clase on se comença a jugar
        .. include:: ./README.md
    """
    __jugador1 = ""
    __jugador2 = ""
    __jugador3 = ""
    __lanzamientos = 0

    def __init__(self, jugador1, jugador2, jugador3, caras1, caras2, caras3, caras4, lanzamientos, intermedios):
        """Constructor de Juego"""
        self.set_jugador1(jugador1)
        self.set_jugador2(jugador2)
        self.set_jugador3(jugador3)
        self.set_lanzamientos(lanzamientos)
        self.dado1 = dado.Dado(caras1)
        self.dado2 = dado.Dado(caras2)
        self.dado3 = dado.Dado(caras3)
        self.dado4 = dado.Dado(caras4)
        # Me guardo en un atributo booelano si necesito o no ver los datos intermedios
        self.__intermedios = (intermedios in ("S", "s"))
        self.resultadoJugador1 = 0
        self.resultadoJugador2 = 0
        self.resultadoJugador3 = 0

    def set_jugador1(self, fjugador1):
        """Comprova el nom al jugador1"""
        if len(fjugador1) > 20:
            raise Exception("la longitud del jugador 1 no ha de ser major de 20")
        else:
            self.__jugador1 = fjugador1

    def set_jugador2(self, fjugador2):
        """Comprova el nom al jugador2"""
        if len(fjugador2) > 20:
            raise Exception("la longitud del jugador 2 no ha de ser major de 20")
        else:
            self.__jugador2 = fjugador2

    def set_jugador3(self, fjugador3):
        """Comprova el nom al jugador3"""
        if len(fjugador3) > 20:
            raise Exception("la longitud del jugador 3 no ha de ser major de 20")
        else:
            self.__jugador3 = fjugador3

    def set_lanzamientos(self, flanzamientos):
        """Comprova el nombre de llançaments"""
        if not 2 < flanzamientos <= 1000:
            raise Exception("El nombre de llançaments te que estar entre 2 i 1000")
        else:
            self.__lanzamientos = flanzamientos

    def jugar(self):
        """Comença el joc"""
        for lanzamiento in range(self.__lanzamientos):
            """Se llançen els daus per a cada jugador y se sumen"""
            # jugador1
            tirada1 = self.dado1.lanzar()
            tirada2 = self.dado2.lanzar()
            tirada3 = self.dado3.lanzar()
            tirada4 = self.dado4.lanzar()
            self.resultadoJugador1 += (tirada1 + tirada2 + tirada3 + tirada4)

            if self.__intermedios:
                print(f"Llançament {lanzamiento + 1}:")
                print(
                    f"{self.__jugador1}: {tirada1} {tirada2} {tirada3} {tirada4} "
                    f"({(tirada1 + tirada2 + tirada3 + tirada4)})")

            # jugador2
            tirada1 = self.dado1.lanzar()
            tirada2 = self.dado2.lanzar()
            tirada3 = self.dado3.lanzar()
            tirada4 = self.dado4.lanzar()
            self.resultadoJugador2 += (tirada1 + tirada2 + tirada3 + tirada4)

            if self.__intermedios:
                print(
                    f"{self.__jugador2}: {tirada1} {tirada2} {tirada3} {tirada4} "
                    f"({(tirada1 + tirada2 + tirada3 + tirada4)})")
                print("")

                # jugador3
                tirada1 = self.dado1.lanzar()
                tirada2 = self.dado2.lanzar()
                tirada3 = self.dado3.lanzar()
                tirada4 = self.dado4.lanzar()
                self.resultadoJugador3 += (tirada1 + tirada2 + tirada3 + tirada4)

                if self.__intermedios:
                    print(
                        f"{self.__jugador3}: {tirada1} {tirada2} {tirada3} {tirada4} "
                        f"({(tirada1 + tirada2 + tirada3 + tirada4)})")
                    print("")

    def mostrarPuntuaciones(self):
        """Es mostra el guanyador"""
        print("Resultats:")
        print(f"Jugador 1: {self.__jugador1}")
        print(f"Jugador 2: {self.__jugador2}")
        print(f"Jugador 3: {self.__jugador3}")
        print(f"Nombre de Llançaments: {self.__lanzamientos}")
        print(f"Daus: {self.dado1.getCaras()},{self.dado2.getCaras()},{self.dado3.getCaras()} y"
              f" {self.dado4.getCaras()}")

        print(f"Punts jugador 1: {self.resultadoJugador1}")
        print(f"Punts jugador 2: {self.resultadoJugador2}")
        print(f"Punts jugador 3: {self.resultadoJugador3}")
        if self.resultadoJugador3 < self.resultadoJugador1 > self.resultadoJugador2:
            print(f"El GUANYADOR es {self.__jugador1} con {self.resultadoJugador1} punts")
        elif self.resultadoJugador1 < self.resultadoJugador2 > self.resultadoJugador3:
            print(f"El GUANYADOR es {self.__jugador2} con {self.resultadoJugador2} punts")
        elif self.resultadoJugador1 < self.resultadoJugador3 > self.resultadoJugador2:
            print(f"El GANADOR es {self.__jugador3} con {self.resultadoJugador3} punts")
        else:
            print("Hi ha hagut un triple EMPATE")
