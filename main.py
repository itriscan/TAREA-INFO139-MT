def strToList(a):
    out = []
    for i in range(len(a)):
        out.append(a[i])
    return out


estadoInicial = input("Ingrese numero del estado Inicial: ")
estadoFinal = input("Ingrese numero del estado Final: ")
estadoActual = estadoInicial

transiciones = [['1', 'a', '2', 'a', 'D'],['2', 'b', '3', 'b', 'D'],['3', 'c', '4', 'c', 'D'],['4', 'a', '2', 'a', 'D'],['4', 'B', '5', 'B', 'I']]
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
    palabra = ["B"] + palabra + ["B"]
    index = 1
    while estadoActual != estadoFinal:
        encontrada = False
        for i in transiciones:
            if (i[0] == str(estadoActual) ) and ( i[1] == palabra[index] ):
                encontrada = True
                print(index,i[2],i[3],i[4])
                estadoActual = i[2]
                palabra[index] = i[3]
                if i[4] == "D":
                    index +=1
                else:
                    index -=1
        if not encontrada:
            print("Palabra no aceptada")
            break
    if encontrada:
        print("Palabra aceptada correctamente")

