from tkinter import ttk
from tkinter import *
from pyswip import Prolog

class Filtro:
    def __init__(self):
        self.__getFiltro()

    def __getFiltro(self):
        self.dialogFiltro = Toplevel()
        self.dialogFiltro.title('Filtro del Bibliofilo')
        
        Label(self.dialogFiltro, text = 'Título: ').grid(row = 1, column = 0)
        titulo = Entry(self.dialogFiltro)
        titulo.focus()
        titulo.grid(row = 1, column = 1)
        estadoCheckTitulo = IntVar()
        tituloCheck = Checkbutton(self.dialogFiltro, text = "No Titulo", variable=estadoCheckTitulo, onvalue = 1, offvalue = 0)
        tituloCheck.grid(row = 1, column = 2)
        

        Label(self.dialogFiltro, text = 'Autor: ').grid(row = 2, column = 0)
        autor = Entry(self.dialogFiltro)
        autor.grid(row = 2, column = 1)
        estadoCheckAutor = IntVar()
        autorCheck = Checkbutton(self.dialogFiltro, text = "No Autor", variable=estadoCheckAutor, onvalue = 1, offvalue = 0)
        autorCheck.grid(row = 2, column = 2)

        Label(self.dialogFiltro, text = 'Categoría: ').grid(row = 3, column = 0)
        categoria = Entry(self.dialogFiltro)
        categoria.grid(row = 3, column = 1)
        estadoCheckCategoria = IntVar()
        categoriaCheck = Checkbutton(self.dialogFiltro, text = "No Categoría", variable=estadoCheckCategoria, onvalue = 1, offvalue = 0)
        categoriaCheck.grid(row = 3, column = 2)

        Label(self.dialogFiltro, text = 'Estado: ').grid(row = 5, column = 0)
        estado = ttk.Combobox(self.dialogFiltro,
        values=[
            "Nuevo",
            "Usado",
            "n/a"
        ])
        estado.grid(row = 5, column = 1)
        estado.current(0)
        estadoCheckEstado = IntVar()
        estadoCheck = Checkbutton(self.dialogFiltro, text = "No Estado", variable=estadoCheckEstado, onvalue = 1, offvalue = 0)
        estadoCheck.grid(row = 5, column = 2)
        
        Label(self.dialogFiltro, text = 'Estado Extra: ').grid(row = 6, column = 0)
        estadoExtra = ttk.Combobox(self.dialogFiltro,
        values=[
            "Porcentaje",
            "Ingreso Extra",
            "Porcentaje e Ingraso Extra"
        ])
        estadoExtra.grid(row = 6, column = 1)
        estadoExtra.current(0)
        estadoCheckestadoExtra = IntVar()
        estadoExtraCheck = Checkbutton(self.dialogFiltro, text = "No Estado Extra", variable=estadoCheckestadoExtra, onvalue = 1, offvalue = 0)
        estadoExtraCheck.grid(row = 6, column = 2)
        estadoExtraCheck.select()

        Label(self.dialogFiltro, text = 'FechaI: ').grid(row = 7, column = 0)
        dia = Entry(self.dialogFiltro)
        dia.grid(row = 7, column = 1)
        mes = Entry(self.dialogFiltro)
        mes.grid(row = 7, column = 2)
        anio = Entry(self.dialogFiltro)
        anio.grid(row = 7, column = 3)
        estadoCheckFechaI = IntVar()
        FechaICheck = Checkbutton(self.dialogFiltro, text = "No FechaI", variable=estadoCheckFechaI, onvalue = 1, offvalue = 0)
        FechaICheck.grid(row = 7, column = 4)

        Label(self.dialogFiltro, text = 'FechaF: ').grid(row = 8, column = 0)
        diaf = Entry(self.dialogFiltro)
        diaf.grid(row = 8, column = 1)
        mesf = Entry(self.dialogFiltro)
        mesf.grid(row = 8, column = 2)
        aniof = Entry(self.dialogFiltro)
        aniof.grid(row = 8, column = 3)
        estadoCheckFechaF = IntVar()
        FechaFCheck = Checkbutton(self.dialogFiltro, text = "No FechaF", variable=estadoCheckFechaF, onvalue = 1, offvalue = 0)
        FechaFCheck.grid(row = 8, column = 4)

        ttk.Button(self.dialogFiltro, text = 'Guardar').grid(row = 9, column = 2)
        
        self.dialogFiltro.mainloop()