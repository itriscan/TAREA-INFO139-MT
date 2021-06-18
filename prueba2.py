from tkinter import*
from typing import List
global c
c = 5
raiz = Tk() 
raiz.title("MT")
raiz.geometry("1660x500")

miFrame = Frame(raiz)
miFrame.pack(fill="both", expand="True")
welcome=Label(miFrame,text="Bienvenid@ a la Maquina de Turing")
welcome.grid(row=0,column=0, columnspan=13)

#------Aqui se define la estructura de como seran ingresadas las transiciones ('EstadoInicial','CaracterInicial')=('EstadoFinal','CaracterFinal','Desplazamiento')---------

def entradaTransiciones(i):
    global c1
    global c2
    global c3
    global c4
    global c5
    delta=Label(miFrame,text="d(")
    delta.grid(row=i, column=0,sticky="e")

    c1 = Entry(miFrame)
    c1.grid(row=i,column=1)
    c1.config(justify="center")
    c2 = Entry(miFrame)
    c2.grid(row=i,column=3)
    c2.config(justify="center")

    coma=Label(miFrame,text=",")
    coma.grid(row=i, column=2)

    parentci=Label(miFrame,text=") = (")
    parentci.grid(row=i,column=4)

    c3 = Entry(miFrame)
    c3.grid(row=i,column=5)
    c3.config(justify="center")
    coma=Label(miFrame,text=",")
    coma.grid(row=i, column=6)

    c4 = Entry(miFrame)
    c4.grid(row=i,column=7)
    c4.config(justify="center")
    coma=Label(miFrame,text=",")
    coma.grid(row=i, column=8)

    c5 = Entry(miFrame)
    c5.grid(row=i,column=9)
    c5.config(justify="center")
    parentc=Label(miFrame,text=")")
    parentc.grid(row=i,column=10)
    botonGuardar=Button(miFrame,text="Guardar",command=guardaTransiciones)
    botonGuardar.grid(row=5,column=13,columnspan=1)
    botonTerminar=Button(miFrame,text="Terminar")
    botonTerminar.grid(row=5,column=14,columnspan=1)


#---------al presionar el boton añadir se hace un llamado a la funcion entradaTransiciones() que crea en la interfaz el recuadro para añadir las transiciones
def añadirTransiciones():
    entradaTransiciones(c)

# crea un arreglo con los datos ingresados en los cuadros de texto de la interfaz 
 # ['EstadoInicial','CaracterInicial','EstadoFinal','CaracterFinal','Desplazamiento']
def creaDelta():

    EstadoInicial = c1.get()
    CaracterInicial = c2.get()
    EstadoFinal = c3.get()
    CaracterFinal = c4.get()
    Dezplazamiento = c5.get()
    delta =[EstadoInicial,CaracterInicial,EstadoFinal,CaracterFinal,Dezplazamiento]
    return delta




def guardaTransiciones():
    delta = creaDelta()
    if(delta[0]=='' or delta[1]=='' or delta[2]=='' or delta[3] == '' or delta[4]==''):
        alerta=Label(miFrame,text="ha quedado una entrada en blanco, reingrese la transicion.")
        alerta.grid(row=122,column=0, columnspan=13)
        delta=creaDelta()
    else:
        alerta=Label(miFrame,text="                              Transicion guardada                                  ")
        alerta.grid(row=122,column=0, columnspan=13)
        A.append(delta)
        print(A)
        c1.delete(0, END)
        c2.delete(0, END)
        c3.delete(0, END)
        c4.delete(0, END)
        c5.delete(0, END)
        return 


def creaArregloTransiciones(A):
    guardaTransiciones()
    return A



botonAñadir=Button(miFrame,text="Añadir",command=añadirTransiciones)
botonAñadir.grid(row=4,column=0,columnspan=1)
A=[]
#creaArregloTransiciones(A)
print(A)
raiz.mainloop()