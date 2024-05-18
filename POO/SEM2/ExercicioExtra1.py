"""Faça um programa que mostre um Menu de Opções para a escolha do usuário:
as opções disponíveis devem ser Soma, Subtrair, Multiplicar, Dividir e Sair. Se o
usuário escolher a opção de somar, subtrair, multiplicar ou dividir o programa
deve chamar a função correspondente, que recebe 2 valores A e B por
parâmetro retorna o resultado da operação. O resultado da operação deve ser
impresso logo após a chamada da função. Quando o usuário escolhe a opção 0
o Programa é encerrado, isto é, a opção Sair é acionada. Obs.: observe que o
exercício é uma adaptação da resolução do exercício da aula anterior"""
from IPython.display import clear_output
def soma(a,b):
    result = a + b
    return result

def multiplicacao(a,b):
    result = a * b
    return result
def subtracao(a,b):
    result = a - b
    if(result < 0):
        result = result *(-1)
    return result

def divisao(a,b):
    result = a/b
    return result

def menuPrincipal():
    global resultado
    clear_output()
    print('\033[94m')
    print('=============================================================')
    print('=                     CALCULADORA SIMPLES                   =')
    print('=============================================================')
    print('=                          OPERAÇÕES                        =')
    print('=                        [ 1 ] - SOMA                       =')
    print('=                        [ 2 ] - SUBTRAÇÃO                  =')
    print('=                        [ 3 ] - MULTIPLICAÇÃO              =')
    print('=                        [ 4 ] - DIVISÃO                    =')
    print('=                        [ 0 ] - SAIR                       =')
    print('=============================================================')
    opcao = int(input('= Digite sua opção:'))
    print('=============================================================')
    if opcao == 1:
        a = int(input('Digite o primeiro valor : '))
        b = int(input('Digite o segundo valor : '))
        resultado = soma(a,b)
        print("A soma entre {} e {} é {}".format(a,b,resultado))
    if opcao == 2:
        a = int(input('Digite o primeiro valor : '))
        b = int(input('Digite o segundo valor : '))
        resultado = subtracao(a, b)
        print("A subtracao entre {} e {} é {}".format(a, b, resultado))
    if opcao == 3:
        a = int(input('Digite o primeiro valor : '))
        b = int(input('Digite o segundo valor : '))
        resultado = multiplicacao(a, b)
        print("A multiplicacao entre {} e {} é {}".format(a, b, resultado))
    if opcao == 4:
        a = int(input('Digite o primeiro valor : '))
        b = int(input('Digite o segundo valor : '))
        if(b==0):
            print('Não existe divisão por 0, tente novamente')
            menuPrincipal()
        else:
            resultado = divisao(a, b)
            print("A multiplicacao entre {} e {} é {}".format(a, b, resultado))
    if opcao == 0:
        clear_output()
        print("\033[43mOBRIGADO POR UTILIZAR A CALCULADORA, PROGRAMA ENCERRADO")

menuPrincipal()

