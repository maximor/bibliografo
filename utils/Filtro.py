from tkinter import ttk
from tkinter import *
from pyswip import Prolog
from entidades import Filtros

class Filtro:
    def __init__(self):
        self.prolog = Prolog()
        self.prolog.consult("ProyectoFinal.pl")
        self.__getFiltro()

    def __getFiltro(self):
        self.dialogFiltro = Toplevel()
        self.dialogFiltro.title('Filtro del Bibliofilo')
        
        Label(self.dialogFiltro, text = 'Título: ').grid(row = 1, column = 0)
        self.titulo = Entry(self.dialogFiltro)
        self.titulo.focus()
        self.titulo.grid(row = 1, column = 1)
        self.estadoCheckTitulo = IntVar()
        self.tituloCheck = Checkbutton(self.dialogFiltro, text = "No Titulo", variable=self.estadoCheckTitulo, onvalue = 1, offvalue = 0)
        self.tituloCheck.grid(row = 1, column = 2)
        

        Label(self.dialogFiltro, text = 'Autor: ').grid(row = 2, column = 0)
        self.autor = Entry(self.dialogFiltro)
        self.autor.grid(row = 2, column = 1)
        self.estadoCheckAutor = IntVar()
        self.autorCheck = Checkbutton(self.dialogFiltro, text = "No Autor", variable=self.estadoCheckAutor, onvalue = 1, offvalue = 0)
        self.autorCheck.grid(row = 2, column = 2)

        Label(self.dialogFiltro, text = 'Categoría: ').grid(row = 3, column = 0)
        self.categoria = Entry(self.dialogFiltro)
        self.categoria.grid(row = 3, column = 1)
        self.estadoCheckCategoria = IntVar()
        self.categoriaCheck = Checkbutton(self.dialogFiltro, text = "No Categoría", variable=self.estadoCheckCategoria, onvalue = 1, offvalue = 0)
        self.categoriaCheck.grid(row = 3, column = 2)

        Label(self.dialogFiltro, text = 'Estado: ').grid(row = 5, column = 0)
        self.estado = ttk.Combobox(self.dialogFiltro,
        values=[
            "Nuevo",
            "Usado",
            "n/a"
        ])
        self.estado.grid(row = 5, column = 1)
        self.estado.current(0)
        self.estadoCheckEstado = IntVar()
        self.estadoCheck = Checkbutton(self.dialogFiltro, text = "No Estado", variable=self.estadoCheckEstado, onvalue = 1, offvalue = 0)
        self.estadoCheck.grid(row = 5, column = 2)
        
        Label(self.dialogFiltro, text = 'Estado Extra: ').grid(row = 6, column = 0)
        self.estadoExtra = ttk.Combobox(self.dialogFiltro,
        values=[
            "Porcentaje",
            "Ingreso Extra",
            "Porcentaje e Ingraso Extra"
        ])
        self.estadoExtra.grid(row = 6, column = 1)
        self.estadoExtra.current(0)
        self.estadoCheckestadoExtra = IntVar()
        self.estadoExtraCheck = Checkbutton(self.dialogFiltro, text = "No Estado Extra", variable=self.estadoCheckestadoExtra, onvalue = 1, offvalue = 0)
        self.estadoExtraCheck.grid(row = 6, column = 2)

        Label(self.dialogFiltro, text = 'FechaI: ').grid(row = 7, column = 0)
        self.dia = Entry(self.dialogFiltro)
        self.dia.grid(row = 7, column = 1)
        self.mes = Entry(self.dialogFiltro)
        self.mes.grid(row = 7, column = 2)
        self.anio = Entry(self.dialogFiltro)
        self.anio.grid(row = 7, column = 3)
        self.estadoCheckFechaI = IntVar()
        self.FechaICheck = Checkbutton(self.dialogFiltro, text = "No FechaI", variable=self.estadoCheckFechaI, onvalue = 1, offvalue = 0)
        self.FechaICheck.grid(row = 7, column = 4)

        Label(self.dialogFiltro, text = 'FechaF: ').grid(row = 8, column = 0)
        self.diaf = Entry(self.dialogFiltro)
        self.diaf.grid(row = 8, column = 1)
        self.mesf = Entry(self.dialogFiltro)
        self.mesf.grid(row = 8, column = 2)
        self.aniof = Entry(self.dialogFiltro)
        self.aniof.grid(row = 8, column = 3)
        self.estadoCheckFechaF = IntVar()
        self.FechaFCheck = Checkbutton(self.dialogFiltro, text = "No FechaF", variable=self.estadoCheckFechaF, onvalue = 1, offvalue = 0)
        self.FechaFCheck.grid(row = 8, column = 4)

        ttk.Button(self.dialogFiltro, text = 'Guardar', command=self.guardar).grid(row = 9, column = 2)
        
        self.dialogFiltro.mainloop()

    def guardar(self):
        titulo = "no"
        autor = "no"
        categoria = "no"
        estado = "no"
        estadoExtra = "no"


        if self.estadoCheckTitulo.get() == 0 and self.titulo.get() != '':
            titulo = self.titulo.get()
    
        if self.estadoCheckAutor.get() == 0 and self.autor.get() != '':
            autor = self.autor.get()
        
        if self.estadoCheckCategoria.get() == 0 and self.categoria.get() != '':
            categoria = self.categoria.get().split(",")

        if self.estadoCheckEstado.get() == 0:
            estado = self.estado.get().lower()

        if self.estadoCheckestadoExtra.get() == 0:
            estadoExtra = self.estadoExtra.get().lower()
        
        self.prolog.assertz("filtrodb("+str(titulo)+","+str(autor)+","+str(categoria)+","+str(estado)+",'"+str(estadoExtra)+"', '2019-20-05')")
        