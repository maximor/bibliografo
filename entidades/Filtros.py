
class Filtro:
    def __init__(self):
        self.__titulo = None
        self.__autor = None
        self.__categoria = []
        self.__raiting = 0
        self.__estado = None
        self.__fechaInicial = None
        self.__fechaFinal = None
        self.__sueldoNeto = 0
        self.__usarSueldoNeto = False
        self.__ingresoExtra = 0

    def setTitulo(self, titulo):
        self.__titulo = titulo

    def getTitulo(self):
        return self.__titulo

    def setAutor(self, autor):
        self.__autor = autor

    def getAutor(self):
        return self.__autor

    def setCagoria(self, categoria):
        if type(categoria) == list:
            self.__categoria = categoria
        else:
            raise Exception('Error de tipo, este metodo recibe una lista')

    def getCategoria(self):
        return self.__categoria

    def setRaiting(self, raiting):
        if raiting > 0 and  raiting <= 5:
            return self.__raiting
        else:
            raise ValueError('Error, el valor del raiting tiene que estar entre 0 y 5 inclusivo')

    def setEstado(self, estado):
        if type(estado) == bool:
            self.__estado = estado
        else:
            raise Exception('Error de tipo, este metodo recibe un booleano')

    def getEstado(self):
        return self.__estado

    def setFechaInicial(self, fechaInicial):
        self.__fechaInicial = fechaInicial

    def getFechaInicial(self):
        return self.__fechaInicial

    def setFechaFinal(self, fechaFinal):
        self.__fechaFinal = fechaFinal

    def getFechaFinal(self):
        return self.__fechaFinal

    def setSueldoNeto(self, sueldoNeto):
        if sueldoNeto > 0:
            self.__sueldoNeto = sueldoNeto
        else:
            raise ValueError('Error, el sueldo neto debe de ser mayor que cero')

    def getSueldoNeto(self):
        return self.__sueldoNeto

    def setUsarSueldoNeto(self, usarSueldoNeto):
        if type(usarSueldoNeto) == bool:
            self.__usarSueldoNeto = usarSueldoNeto
        else:
            raise Exception('Error de tipo, este metodo recibe un booleano')

    def usarSueldoNeto(self):
        return self.__usarSueldoNeto

    def setIngrsoExtra(self, ingresoExtra):
        if ingresoExtra > 0:
            self.__ingresoExtra = ingresoExtra
        else:
            raise ValueError('Error, el ingreso extra debe de ser mayor que cero')

    def getIngrsoExtra(self):
        return self.__ingresoExtra