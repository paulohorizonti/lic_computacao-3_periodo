#Lista que ira receber os falores
def lerValores():
    lista_a = [] #Criacao da lista
    for i in range(0,5): #for de 0 ate 5
        aux = input(f'Digite o {i+1}º valor : ') #salva em variavel auxiliar
        lista_a.append(aux) #Acrescenta à lista
    return lista_a #retorna a lista

#Funcao para imprimir a lista
def imprimirValores(lista): #recebe a lista como parametro
    for i in range(len(lista)): #faz um range no tamanho da lista
        print(f'O {i+1}º valor é : ',lista[i]) #imprimi os valores na tela

listaVAl = lerValores() #chama a funcao de ler os valores
imprimirValores(listaVAl) #chama a funcao de imprimir os valores passando a lista como parametro