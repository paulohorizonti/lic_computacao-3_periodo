def lerValores(n):
    listaDeValores = []
    for i in range(n):
        listaDeValores.append(i+1)
    return listaDeValores

def valoresPares(listaValores):
    listaValoresPares=[]
    for valor in listaValores:
        if(valor % 2 == 0):
            listaValoresPares.append(valor)
    return listaValoresPares

def valoresImpares(listaValores):
    listaValoresImpares=[]
    for valor in listaValores:
        if(valor %2 !=0):
            listaValoresImpares.append(valor)
    return listaValoresImpares

def imprimirValores(listaValores):
    for i in range(len(listaValores)):
        print(f"O valor {i+1} é ",listaValores[i])

valoresEntrada = lerValores(10)
print(valoresEntrada)
print(valoresPares(valoresEntrada))
print(valoresImpares(valoresEntrada))