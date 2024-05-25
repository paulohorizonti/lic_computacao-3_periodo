def imprimirMenu():
    while True:
        print("MENU DE OPCOES")
        print("1. somar a e b")
        print("2 subtrair a e b")
        print("3 - multiplicar a e b")
        print("4 - Dividir a e b")
        print("0 - sair")
        opcao = int(input("\nDigite a opcao desejada"))
        if opcao == 0:
            break
        elif opcao == 1:
            a = float(input("Digite o valor de a: "))
            b = float(input("Digite o valor de b: "))
            resultado = somar(a,b)
            print("O resultado da operacao é: ",resultado)
imprimirMenu()