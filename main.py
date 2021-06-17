def strToList(a):
    out = []
    for i in range(len(a)):
        out.append(a[i])
    return out


estadoInicial = input("Ingrese numero del estado Inicial: ")
estadoFinal = input("Ingrese numero del estado Final: ")
estadoActual = estadoInicial

transiciones = []
q = False

while q == False:
    ## Se toma una entrada, la cual consta de 5 elementos y se ordenan de la misma forma vista en clases
    # ['Estado inicial','CaracterInicial','EstadoFinal','CaracterFinal','Desplazamiento']
    entr = input()
    if entr != "q":
        entr = entr.split(",")
        transiciones.append(entr)
    else:
        q = True
    print(entr)


palabraEntrada = input()
if palabraEntrada != "":
    print("Palabra distinta de vacio")
    palabra = strToList(palabraEntrada)
    print(palabra)
    index = 0

    ##while estadoActual != estadoFinal:
        ##Cosas, muchas
    

    for i in transiciones:
        if (i[0] == str(estadoActual) ) and ( i[1] == palabraEntrada[index] ):
            print("true",i[2],i[3],i[4])
            estadoActual = i[2]
            palabra[index] = i[3]
            if i[4] == "D":
                index +=1
            else:
                index -=1


    print(transiciones,palabra,estadoActual)