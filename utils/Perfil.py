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

        # Label(self.dialogPerfil, text = 'condición: ').grid(row = 3, column = 0)
        # self.condicion = ttk.Combobox(self.dialogPerfil,
        # values=[
        #     "Porcentaje",
        #     "Ingreso Extra",
        #     "Porcentaje e Intraso Extra"
        # ])
        # self.condicion.grid(row = 3, column = 1)

        Label(self.dialogPerfil, text = 'Porcentaje: ').grid(row = 4, column = 0)
        self.porcentaje = Entry(self.dialogPerfil)
        self.porcentaje.grid(row = 4, column = 1)

        Label(self.dialogPerfil, text = 'Sueldo Ext.: ').grid(row = 5, column = 0)
        self.sueldoEx = Entry(self.dialogPerfil)
        self.sueldoEx.grid(row = 5, column = 1)

        ttk.Button(self.dialogPerfil, text = 'Guardar', command= self.guardar).grid(row = 6, column = 0)

        #Cargando la configuracion 
        if self.existeBibliografo():
            bibliografo = list(self.prolog.query("bibliografo(X,Y)"))
            self.nameAux = bibliografo[0]["X"]
            self.sueldoAux = bibliografo[0]["Y"]

            self.name.insert(0, self.nameAux)
            self.sueldo.insert(0, self.sueldoAux)

        if self.existeBibliografoEx():
            bibliografoEx = list(self.prolog.query("bibliografoEx(X,Y)"))
            self.porcentajeAux = bibliografoEx[0]["X"]
            self.sueldoExAux = bibliografoEx[0]["Y"]

            self.porcentaje.insert(0, self.porcentajeAux)
            self.sueldoEx.insert(0, self.sueldoExAux)

        self.dialogPerfil.mainloop()

    def guardar(self):
        if self.existeBibliografo() == False:
            if self.name.get() != '' and self.sueldo.get() != '':
                self.prolog.assertz("bibliografo("+self.name.get()+","+self.sueldo.get()+")")
            
            if self.porcentaje.get() != '':
                self.prolog.assertz("bibliografoEx("+self.porcentaje.get()+",0)")
            elif self.sueldoEx.get() != '':
                self.prolog.assertz("bibliografoEx(0,"+self.sueldoEx.get()+")")
            else:
                self.prolog.assertz("bibliografoEx(0,0)")

        else: 
            list(self.prolog.query("actualizarSueldo("+self.sueldo.get()+")"))
            if self.porcentaje.get() != '' or self.sueldoEx.get() != '':
                if self.existeBibliografoEx() == False:
                    self.prolog.assertz("bibliografoEx("+self.porcentaje.get()+","+self.sueldoEx.get()+")")
                else:
                    if self.existeBibliografoEx():
                        for i in self.prolog.query("retract(bibliografoEx(_,_)),fail"):
                            print
                    if self.porcentaje.get() != '' and self.sueldoEx.get() == '':
                        self.prolog.assertz("bibliografoEx("+self.porcentaje.get()+",0)")
                    elif self.sueldoEx.get() != '' and self.porcentaje.get() == '':
                        self.prolog.assertz("bibliografoEx(0,"+self.sueldoEx.get()+")")
                    else:
                        self.prolog.assertz("bibliografoEx("+self.porcentaje.get()+","+self.sueldoEx.get()+")")

    def existeBibliografo(self):
        return len(list(self.prolog.query("bibliografo(X,Y)"))) > 0

    def existeBibliografoEx(self):
        return len(list(self.prolog.query("bibliografoEx(X,Y)"))) > 0