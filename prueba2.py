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
def creaArregloTransiciones():
    A = []
    L = True
    while L:
        deltsi=guardaTransiciones()
        A+=[deltsi]
        print(A)
    return

def entradaTransiciones(i):
    delta=Label(miFrame,text="d(")
    delta.grid(row=i, column=0,sticky="e")
    global c1
    global c2
    global c3
    global c4
    global c5
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
    botonTerminar=Button(miFrame,text="Terminar",command=creaArregloTransiciones)
    botonTerminar.grid(row=5,column=14,columnspan=1)
    
def añadirTransiciones():
    entradaTransiciones(c)


 # ['Estado inicial','CaracterInicial','EstadoFinal','CaracterFinal','Desplazamiento'
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
    return delta




botonAñadir=Button(miFrame,text="Añadir",command=añadirTransiciones)
botonAñadir.grid(row=4,column=0,columnspan=1)


raiz.mainloop()