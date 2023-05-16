class Dado:
    """Class On es Construeix el dau"""
    __caras = 6
    __caras_utilizadas = []

    def __init__(self, fcaras):
        """Es construeix el dau"""
        self.setCaras(fcaras)

    def lanzar(self):
        """Es llança el dau"""
        import random
        return random.randint(1, self.__caras)

    def getCaras(self):
        """
        Torna el nombre de cares del dau
        :return: int
        """
        return self.__caras

    def setCaras(self, fcaras):
        """Comprova si els daus que li pasen te les cares permitides"""
        caras_permitidas = [4, 6, 8, 10, 12, 20, 120, 200, 300]
        if fcaras in caras_permitidas and fcaras not in self.__caras_utilizadas:
            self.__caras = fcaras
            print(fcaras)
            self.__caras_utilizadas.append(fcaras)
            print(self.__caras_utilizadas)
        else:
            raise Exception("Nombre de cares incorrecte")
