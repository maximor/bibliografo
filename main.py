from tkinter import ttk
from tkinter import *
from utils import Perfil
from utils import Filtro
from pyswip import Prolog

class Aplicacion():
    def __init__(self, main):
        #cargamos los datos de prolog aqui
        self.prolog = Prolog()
        self.cargarBaseBibliografo()
        self.perfil = Perfil.Perfil
        self.filtro = Filtro.Filtro

        self.main = main
        self.main.title('Titulo de la aplicacion')
        self.main.geometry('1008x650')

        #Creando el header frame de la aplicacion
        frameCabeza = LabelFrame(self.main, text='Opciones')
        frameCabeza.grid(row=0, column=0)

        #Creacion de botones para lanzar las configuraciones
        ttk.Button(frameCabeza,text="Filtros", command=self.filtro).grid(row=0, column=0)
        ttk.Button(frameCabeza,text='Perfil', command=self.perfil).grid(row=0, column=1)

        #Creando un con Frame para contener los datos de la izquierda
        frameIzquierdo = LabelFrame(self.main, text = 'Lista de libros')
        frameIzquierdo.grid(row=1, column=0)

        frameDerecho = LabelFrame(self.main, text = 'Sugerencias')
        frameDerecho.grid(row=3, column=0)

        #Tabla para presentar todos los libros
        self.tablaIzquierda = ttk.Treeview(frameIzquierdo,
        columns=('Autor', 'Genero', 'Precio', 'Rating','Fecha', 'ISBN'), height=15)
        self.tablaIzquierda.grid(row=4, column=0)
        self.tablaIzquierda.heading('#0', text='Titulo')
        self.tablaIzquierda.column('#0', minwidth=0, width=200, stretch=NO)

        self.tablaIzquierda.heading('#1', text='Autor')
        self.tablaIzquierda.column('#1', minwidth=0, width=200, stretch=NO)

        self.tablaIzquierda.heading('#2', text='Genero')
        self.tablaIzquierda.column('#2', minwidth=0, width=200, stretch=NO)

        self.tablaIzquierda.heading('#3', text='Precio')
        self.tablaIzquierda.column('#3', minwidth=0, width=100, stretch=NO)

        self.tablaIzquierda.heading('#4', text='Rating')
        self.tablaIzquierda.column('#4', minwidth=0, width=100, stretch=NO)

        self.tablaIzquierda.heading('#5', text='Fecha')
        self.tablaIzquierda.column('#5', minwidth=0, width=100, stretch=NO)

        self.tablaIzquierda.heading('#6', text='ISBN')
        self.tablaIzquierda.column('#6', minwidth=0, width=100, stretch=NO)

        #llenando la tabla superior
        for libro in self.prolog.query("libro(T,A,G,P,D,R,_,_)"):
            self.tablaIzquierda.insert('', 
            0, 
            text=libro["T"], 
            value=(libro["A"],
            libro["G"],
            libro["P"],
            libro["R"],
            libro["D"]))

        #Tabla para presentar las sugerencias
        self.tablaDerecha = ttk.Treeview(frameDerecho,
        columns=('Autor', 'Genero', 'Precio', 'Rating', 'Fecha', 'ISBN'), height=10)
        self.tablaDerecha.grid(row=4, column=0)
        self.tablaDerecha.heading('#0', text='Titulo')
        self.tablaDerecha.column('#0', minwidth=0, width=200, stretch=NO)

        self.tablaDerecha.heading('#1', text='Autor')
        self.tablaDerecha.column('#1', minwidth=0, width=200, stretch=NO)

        self.tablaDerecha.heading('#2', text='Genero')
        self.tablaDerecha.column('#2', minwidth=0, width=200, stretch=NO)

        self.tablaDerecha.heading('#3', text='Precio')
        self.tablaDerecha.column('#3', minwidth=0, width=100, stretch=NO)

        self.tablaDerecha.heading('#4', text='Rating')
        self.tablaDerecha.column('#4', minwidth=0, width=100, stretch=NO)

        self.tablaDerecha.heading('#5', text='Fecha')
        self.tablaDerecha.column('#5', minwidth=0, width=100, stretch=NO)

        self.tablaDerecha.heading('#6', text='ISBN')
        self.tablaDerecha.column('#6', minwidth=0, width=100, stretch=NO)

    def cargarBaseBibliografo(self):
        self.prolog.consult("ProyectoFinal.pl")
        for i in self.prolog.query("bibliografo(X,Y)"):
            print(i)

if __name__ == '__main__':
    main = Tk()
    aplicacion = Aplicacion(main)
    main.mainloop()