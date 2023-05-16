class Dado:
    __caras = 6
    __caras_utilizadas = []

    def __init__(self, fcaras):
        self.setCaras(fcaras)

    def lanzar(self):
        import random
        return random.randint(1, self.__caras)

    def getCaras(self):
        return self.__caras

    def setCaras(self, fcaras):
        caras_permitidas = [4, 6, 8, 10, 12, 20, 120, 200, 300]
        if fcaras in caras_permitidas and fcaras not in self.__caras_utilizadas:
            self.__caras = fcaras
            print(fcaras)
            self.__caras_utilizadas.append(fcaras)
            print(self.__caras_utilizadas)
        else:
            raise Exception("Numero de caras incorrecto")
