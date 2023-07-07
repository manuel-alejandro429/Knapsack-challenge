

def maximizarElementos_Mochila(lista, peso_maximo):
    cantidad_elementos = len(lista)

    #Creo una lista llena de ceros que se repiten (peso_maximo + 1) veces
    #En esta lista se almacenaran mas adelante valores máximos o mas optimos
    valores_maximos = [0] * (peso_maximo + 1)

    #Con los siguientes for anidados calculo dichos valores máximos
    for x in range(cantidad_elementos):
        pesoMomentaneo = lista[x][0]
        valorMomentaneo = lista[x][1]
        for y in range(peso_maximo, pesoMomentaneo - 1, -1):
            nuevo_valor = valorMomentaneo + valores_maximos[y - pesoMomentaneo]
            if nuevo_valor > valores_maximos[y]:
                valores_maximos[y] = nuevo_valor


    #Aquí se empieza a construir la combinación mas adecuada a partir de la lista de valores mas optimos
    elementos_seleccionados = [] #Aquí se creara la lista de elementos que finalmente serán seleccionados
    pesoActual = peso_maximo
    for a in range(cantidad_elementos - 1, -1, -1): #itero en orden inverso sobre los índices de los elementos
        peso_elemento = lista[a][0]
        valor_elemento = lista[a][1]
        #El siguiente if exteso es para determinar si el elemento si debe ir en la mochila
        if (peso_elemento <= pesoActual) and (valores_maximos[pesoActual] == (valor_elemento + valores_maximos[pesoActual - peso_elemento])):
            elementos_seleccionados.append(lista[a])
            pesoActual = pesoActual - peso_elemento

    return elementos_seleccionados


#Esta es la prueba que se brinda en el pdf de guía
pesoMaximo_prueba = 10
elementos = [(2, 3), (3, 4), (4, 5), (5, 6)]


#Esta es otra lista de elementos para probar el funcionamiento
pesoMaximo_prueba2 = 25
elementos2 = [(7,5),(12,4),(14,0),(21,3),(2,21),(7,4),(3,2)]



elementosSeleccionar = maximizarElementos_Mochila(elementos, pesoMaximo_prueba)
print(elementosSeleccionar)

print("---------------------------------------------------")

elementosSeleccionar2 = maximizarElementos_Mochila(elementos2, pesoMaximo_prueba2)
print(elementosSeleccionar2)