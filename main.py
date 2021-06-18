def strToList(a):
    out = []
    for i in range(len(a)):
        out.append(a[i])
    return out


estadoInicial = input("Ingrese numero del estado Inicial: ")
estadoFinal = input("Ingrese numero del estado Final: ")


transiciones = [['0','a','1','X','D'],['0','Y','3','Y','D'],['1','a','1','a','D'],['1','b','2','Y','I'],['1','Y','1','Y','D'],['2','a','2','a','I'],['2','X','0','X','D'],['2','Y','2','Y','I'],['3','b','4','Y','D'],['3','Y','3','Y','D'],['4','b','4','Y','D'],['4','B','5','B','I']]
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


palabraEntrada = input()
while palabraEntrada != "q":
    print("Probando palabra: ",palabraEntrada)
    estadoActual = estadoInicial
    palabra = strToList(palabraEntrada)
    palabra = ["B"] + palabra + ["B"]
    index = 1
    while estadoActual != estadoFinal:
        encontrada = False
        for i in transiciones:
            if (i[0] == str(estadoActual) ) and ( i[1] == palabra[index] ):
                encontrada = True
                estadoActual = i[2]
                palabra[index] = i[3]
                if i[4] == "D":
                    index +=1
                elif i[4] == "I":
                    index -=1
                break
        if not encontrada:
            print("Palabra no aceptada")
            break
    if encontrada:
        print("Palabra aceptada correctamente")
    palabraEntrada = input()
