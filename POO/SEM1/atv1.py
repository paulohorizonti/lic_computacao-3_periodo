from IPython.display import clear_output
def subtrai():
    global a, b
    a = float(input("DIGITE O VALOR DE A: "))
    b = float(input("DIGITE O VALOR DE B: "))
    sub = a - b
    print("A subtracao DE A + B É: ", sub, "\n\n")

def soma():
    global a,b
    a = float(input("DIGITE O VALOR DE A: "))
    b = float(input("DIGITE O VALOR DE B: "))
    soma = a+b
    print("A SOMA DE A + B É: ", soma,"\n\n")

def imprimirMenu():
    while True:
        print("<---- MENU DE OPÇÕES ---->\n")
        print("1 SOMA A + B\n")
        print("0 SAIR\n")
        opcao = int(input("\n\nDIGITE A OPCAO DESEJADA: "))
        if opcao == 0:
            break
        elif opcao ==1:

            soma()
        elif opcao == 2:
            clear_output()
            subtrai()
imprimirMenu()


