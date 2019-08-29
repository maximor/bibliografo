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
        self.main.geometry('1020x650')
        self.main.resizable(width=0, height=0)

        #Creando el header frame de la aplicacion
        frameCabeza = LabelFrame(self.main, text='Opciones')
        frameCabeza.grid(row=0, column=0)

        #Creacion de botones para lanzar las configuraciones
        ttk.Button(frameCabeza,text="Filtros", command=self.filtro).grid(row=0, column=0)
        ttk.Button(frameCabeza,text='Perfil', command=self.perfil).grid(row=0, column=1)
        ttk.Button(frameCabeza,text='Filtrar', command=self.filtrar).grid(row=0, column=2)
        #Creando un con Frame para contener los datos de la izquierda
        frameIzquierdo = LabelFrame(self.main, text = 'Lista de libros')
        frameIzquierdo.grid(row=1, column=0)

        frameDerecho = LabelFrame(self.main, text = 'Sugerencias')
        frameDerecho.grid(row=3, column=0)

        #Tabla para presentar todos los libros
        self.tablaIzquierda = ttk.Treeview(frameIzquierdo,
        columns=('Autor', 'Genero', 'Precio', 'Rating','Fecha', 'Estado'), height=15)

        #poniendo el scrollbar en la tabla
        vsb = ttk.Scrollbar(self.main, orient="vertical", command=self.tablaIzquierda.yview)
        vsb.place(x=985, y=86, height=300)
        self.tablaIzquierda.configure(yscrollcommand=vsb.set)

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

        self.tablaIzquierda.heading('#6', text='Estado')
        self.tablaIzquierda.column('#6', minwidth=0, width=100, stretch=NO)

        #llenando la tabla superior
        for libro in self.prolog.query("libro(T,A,G,P,D,R,E,_)"):
            self.tablaIzquierda.insert('', 
            0, 
            text=libro["T"], 
            value=(libro["A"],
            libro["G"],
            libro["P"],
            libro["R"],
            libro["D"],
            libro["E"]))

        #Tabla para presentar las sugerencias
        self.tablaDerecha = ttk.Treeview(frameDerecho,
        columns=('Autor', 'Genero', 'Precio', 'Rating', 'Fecha', 'Estado'), height=10)

        #poniendo el scrollbar en la tabla
        vsb2 = ttk.Scrollbar(self.main, orient="vertical", command=self.tablaDerecha.yview)
        vsb2.place(x=985, y=430, height=203)
        self.tablaDerecha.configure(yscrollcommand=vsb2.set)

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

        self.tablaDerecha.heading('#6', text='Estado')
        self.tablaDerecha.column('#6', minwidth=0, width=100, stretch=NO)

    def cargarBaseBibliografo(self):
        self.prolog.consult("ProyectoFinal.pl")
        # for i in self.prolog.query("disponiblecompra(5000,10,1000,2)"):
        #     print(i)

        # for i in self.prolog.query("filtro(Titulo,Autor,Genero,Precio,Fecha,Raiting,Estado,ISBN)"):
        #     print(i)

        # libros = {}
        # for i in self.prolog.query("resultado(libro(Titulo,Autor,Genero,Precio,Fecha,Raiting,Estado,_))"):
        #     libros[i["Titulo"]] = i 
        
        # print(libros)

    def filtrar(self):
        for i in self.tablaDerecha.get_children():
            self.tablaDerecha.delete(i)

        if len(list(self.prolog.query("bibliografo(X,Y)"))) > 0:
            for bibliografo in list(self.prolog.query("bibliografo(X,Y)")):
                if len(list(self.prolog.query("bibliografoEx(W,Z)"))) > 0:
                    for bibliografoEx in list(self.prolog.query("bibliografoEx(W,Z)")):
                        if len(list(self.prolog.query("filtrodb(T,A,C,E,EE,D)"))) == 0:
                            for i in self.prolog.query("disponiblecompra("+str(bibliografo["Y"])+","+str(bibliografoEx["W"])+","+str(bibliografoEx['Z'])+",2)"):
                                print
                            for i in self.prolog.query("filtro(Titulo,Autor,Genero,Precio,Fecha,Raiting,Estado,ISBN)"):
                                print

                            general = {}
                            #llenando la tabla superior
                            for libro in self.prolog.query("resultado(libro(Titulo,Autor,Genero,Precio,Fecha,Raiting,Estado,_))"):
                                general[libro["Titulo"]] = [libro['Titulo'],libro['Autor'],libro['Genero'],libro['Precio'],libro['Fecha'],libro['Raiting'],libro['Estado']]
                            
                            for key, val in general.items():
                                self.tablaDerecha.insert('',
                                0,text=val[0],
                                value=(val[1],
                                val[2],
                                val[3],
                                val[5],
                                val[4],
                                val[6]))
                        else:
                            for filtrodb in list(self.prolog.query("filtrodb(T,A,C,E,EE,D)")):
                                print(filtrodb)
                                titulo = "Titulo"
                                autor = "Autor"
                                categoria = "Categoria"
                                ee = 2
                                if filtrodb['T'] != "no":
                                    titulo = filtrodb["T"]
                                if filtrodb["A"] != "no":
                                    autor = filtrodb["A"]
                                if filtrodb["C"] != "no":
                                    categoria = filtrodb["A"]
                                if filtrodb["EE"] == "porcentaje":
                                    ee = 1
                                elif filtrodb["EE"] == "ingreso extra":
                                    ee = 2
                                else: 
                                    ee = 3

                                for i in self.prolog.query("disponiblecompra("+str(bibliografo["Y"])+","+str(bibliografoEx["W"])+","+str(bibliografoEx['Z'])+","+str(ee)+")"):
                                    print
                                for i in self.prolog.query("filtro("+str(titulo)+","+str(autor)+","+str(categoria)+",Precio,Fecha,Raiting,"+str(filtrodb["E"])+",ISBN)"):
                                    print

                                general = {}
                                #llenando la tabla superior
                                for libro in self.prolog.query("resultado(libro(Titulo,Autor,Genero,Precio,Fecha,Raiting,Estado,_))"):
                                    general[libro["Titulo"]] = [libro['Titulo'],libro['Autor'],libro['Genero'],libro['Precio'],libro['Fecha'],libro['Raiting'],libro['Estado']]
                            
                                for key, val in general.items():
                                    self.tablaDerecha.insert('',
                                    0,text=val[0],
                                    value=(val[1],
                                    val[2],
                                    val[3],
                                    val[5],
                                    val[4],
                                    val[6]))
if __name__ == '__main__':
    main = Tk()
    aplicacion = Aplicacion(main)
    main.mainloop()