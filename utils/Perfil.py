from tkinter import ttk
from tkinter import *
from pyswip import Prolog

class Perfil:
    def __init__(self):
        self.prolog = Prolog()
        self.prolog.consult("ProyectoFinal.pl")
        self.__getPerfil()
        
    def __getPerfil(self):
        self.dialogPerfil = Toplevel()
        self.dialogPerfil.title('Perfil del Bibliofilo')
        Label(self.dialogPerfil, text='Nombre: ').grid(row = 1, column = 0)
        self.name = Entry(self.dialogPerfil)
        self.name.focus()
        self.name.grid(row=1,column=1)

        Label(self.dialogPerfil, text='Sueldo: ').grid(row = 2, column = 0)
        self.sueldo = Entry(self.dialogPerfil)
        self.sueldo.grid(row = 2, column = 1)

        ttk.Button(self.dialogPerfil, text = 'Guardar', command= self.guardar).grid(row = 3, column = 0)

        #Cargando la configuracion 
        if self.existeBibliografo():
            bibliografo = list(self.prolog.query("bibliografo(X,Y)"))
            self.nameAux = bibliografo[0]["X"]
            self.sueldoAux = bibliografo[0]["Y"]

            self.name.insert(0, self.nameAux)
            self.sueldo.insert(0, self.sueldoAux)

        self.dialogPerfil.mainloop()

    def guardar(self):
        if self.existeBibliografo() == False:
            if self.name.get() != '' and self.sueldo.get() != '':
                self.prolog.assertz("bibliografo("+self.name.get()+","+self.sueldo.get()+")")
        else: 
            self.prolog.query("actualizarSueldo("+self.sueldo.get()+")")

    def existeBibliografo(self):
        return len(list(self.prolog.query("bibliografo(X,Y)"))) > 0