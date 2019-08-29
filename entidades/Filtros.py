
class Filtro:
    def __init__(self):
        self.__titulo
        self.__autor
        self.__categoria
        self.__estado
        self.__estadoExtra
        self.__fechaInicial
        self.__fechaFinal

    @staticmethod
    def setTitulo(self, titulo):
        self.__titulo = titulo

    @staticmethod
    def getTitulo(self):
        return self.__titulo
    
    @staticmethod
    def setAutor(self, autor):
        self.__autor = autor

    @staticmethod
    def getAutor(self):
        return self.__autor

    @staticmethod
    def setCagoria(self, categoria):
        if type(categoria) == list:
            self.__categoria = categoria
        else:
            raise Exception('Error de tipo, este metodo recibe una lista')

    @staticmethod
    def getCategoria(self):
        return self.__categoria

    @staticmethod
    def setEstado(self, estado):
        if type(estado) == bool:
            self.__estado = estado
        else:
            raise Exception('Error de tipo, este metodo recibe un booleano')

    @staticmethod
    def getEstado(self):
        return self.__estado

    @staticmethod
    def setFechaInicial(self, fechaInicial):
        self.__fechaInicial = fechaInicial
        
    @staticmethod
    def getFechaInicial(self):
        return self.__fechaInicial

    @staticmethod
    def setFechaFinal(self, fechaFinal):
        self.__fechaFinal = fechaFinal

    @staticmethod
    def getFechaFinal(self):
        return self.__fechaFinal