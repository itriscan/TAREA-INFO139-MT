def strToList(a):
    out = []
    for i in range(len(a)):
        out.append(a[i])
    return out

def probarPalabra(a,transiciones,inicial,final):
    print("Probando palabra: ",a)
    estadoActual = inicial
    palabra = strToList(a)
    palabra = ["B"] + palabra + ["B"]
    index = 1
    while estadoActual != final:
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
            return (False)
    if encontrada:
        print("Palabra aceptada correctamente")
    return (True)
