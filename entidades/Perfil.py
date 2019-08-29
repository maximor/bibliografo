
class Perfil:

    def __init__(self):
        self.__nombre = None
        self.__sueldo = 0

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getNombre(self):
        return self.__nombre

    def setSueldo(self, sueldo):
        if sueldo > 0:
            self.__sueldo = sueldo
        else:
            raise ValueError('Error, el valor del sueldo debe de ser mayor que cero')

    def getSueldo(self):
        return self.__sueldo