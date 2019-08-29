from tkinter import ttk
from tkinter import *

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

        Label(self.dialogFiltro, text = 'Autor: ').grid(row = 2, column = 0)
        autor = Entry(self.dialogFiltro)
        autor.grid(row = 2, column = 1)

        Label(self.dialogFiltro, text = 'Categoría: ').grid(row = 3, column = 0)
        categoria = Entry(self.dialogFiltro)
        categoria.grid(row = 3, column = 1)

        Label(self.dialogFiltro, text = 'Rating: ').grid(row = 4, column = 0)
        rating = ttk.Combobox(self.dialogFiltro,
        values=[1,2,3,4,5])
        rating.grid(row = 4, column = 1)
        rating.current(0)

        Label(self.dialogFiltro, text = 'Estado: ').grid(row = 5, column = 0)
        estado = ttk.Combobox(self.dialogFiltro,
        values=[
            "Nuevo",
            "Usado",
            "n/a"
        ])
        estado.grid(row = 5, column = 1)
        estado.current(0)

        Label(self.dialogFiltro, text = 'Fecha Inicial: ').grid(row = 6, column = 0)
        dia = Entry(self.dialogFiltro, width = 5)
        dia.grid(row = 6, column = 1)
        mes = Entry(self.dialogFiltro, width = 5)
        mes.grid(row = 6, column = 2)
        anio = Entry(self.dialogFiltro, width = 5)
        anio.grid(row = 6, column = 3)
        
        self.dialogFiltro.mainloop()