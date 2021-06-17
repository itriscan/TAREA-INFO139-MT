from tkinter import*
#estado = bool()
raiz = Tk()
raiz.title("MT")
raiz.geometry("5000x3000")

miFrame = Frame(raiz)
miFrame.pack(fill="both", expand="True")
welcome=Label(miFrame,text="Bienvenid@ a la Maquina de Turing")
welcome.grid(row=0,column=0, columnspan=13)

#def empezarBoton():
#   estado.set(True)

#   return estado
#botonEmpezar=Button(miFrame,text="Empezar", command=empezarBoton)
#botonEmpezar.grid(row=0,column=1)


# la funcion EntradaTransiciones es para mostrar el espacion donde se escribiran las transiciones
# estas seran escritas de la forma d(nodo_inicial, caracter_que_lee)=(nodo_destino, caracter que escribe, desplazamiento)
def entradaTransiciones():
    delta=Label(miFrame,text="d(")
    delta.grid(row=3, column=0,sticky="e")

    c1 = Entry(miFrame)
    c1.grid(row=3,column=1)
    c1.config(justify="center")
    c2 = Entry(miFrame)
    c2.grid(row=3,column=3)
    c2.config(justify="center")

    coma=Label(miFrame,text=",")
    coma.grid(row=3, column=2)

    parentci=Label(miFrame,text=") = (")
    parentci.grid(row=3,column=4)

    c3 = Entry(miFrame)
    c3.grid(row=3,column=5)
    c3.config(justify="center")
    coma=Label(miFrame,text=",")
    coma.grid(row=3, column=6)

    c4 = Entry(miFrame)
    c4.grid(row=3,column=7)
    c4.config(justify="center")
    coma=Label(miFrame,text=",")
    coma.grid(row=3, column=8)

    c5 = Entry(miFrame)
    c5.grid(row=3,column=9)
    c5.config(justify="center")
    parentc=Label(miFrame,text=")")
    parentc.grid(row=3,column=10)

    botonGuardar=Button(miFrame,text="Guardar")
    botonGuardar.grid(row=3,column=11)
    botonTerminar=Button(miFrame,text="Terminar")
    botonTerminar.grid(row=3,column=13)





# Funcion para definir el estado inicial y el estado final

def codigoBoton():
    global inicial
    global final
    inicial= c6.get()
    final = c7.get()

text1=Label(miFrame,text="Estado inicial: ")
text1.grid(row=1, column=0,sticky="e")
c6 = Entry(miFrame)
c6.grid(row=1,column=1)
c6.config(justify="center")

text2=Label(miFrame,text="Estado final: ")
text2.grid(row=2, column=0,sticky="e")
c7 = Entry(miFrame)
c7.grid(row=2,column=1)
c7.config(justify="center")
botonGuardar1=Button(miFrame,text="Guardar",command=codigoBoton)
botonGuardar1.grid(row=2,column=3)

#------------Estado Inicial y Final guardados en las variables inicial y final respectivamente

# Funcion para guardar la 'Palabra' de entrada

def guardarPalabra():
    global palabra
    palabra = c8.get()


text1=Label(miFrame,text="Palabra: ")
text1.grid(row=10, column=0,sticky="e")
c8 = Entry(miFrame)
c8.grid(row=10,column=1)
c8.config(justify="center")
botonGuardar2=Button(miFrame,text="Guardar", command=guardarPalabra)
botonGuardar2.grid(row=10,column=3)
#-----------------palabra de entrada guardada en la variable pal------------


Empezar = False
if Empezar==True:
    entradaTransiciones()




raiz.mainloop()
print("Estado inicial: "+ inicial)
print("Estado final: "+ final)
print("la palabra es: "+ palabra)
EIF = [final,inicial]
print(E)