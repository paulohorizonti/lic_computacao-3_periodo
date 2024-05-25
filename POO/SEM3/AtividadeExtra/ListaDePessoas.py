"""Faça um programa que disponibilize ao usuário um menu de opções que
permita o usuário inserir pessoas em uma lista, consultar uma determinada
pessoa cadastrada pelo cpf e imprmir todos os seus dados, e uma opção sair,
que será acionada caso o usuário escolha a opção 0. A classe pessoa deve ter
os seguintes atributos: nome, rg e cpf. """
class Pessoa:
    def __init__(self, nome=None, rg=None, cpf=None):
        self.nome = nome
        self.rg = rg
        self.cpf = cpf

def CadastrarPessoa():
    pessoa = Pessoa()
    pessoa.nome = input("Digite o nome da Pessoa: ")
    pessoa.rg = input("Digite o RG da pessoa: ")
    pessoa.cpf = input("Digite o CPF da Pessoa: ")
    pessoas.append(pessoa)
def PesquisaCPF():
    cpf = input("QUAL CPF A SER PROCURADO? ")
    for pessoa in pessoas:
        if pessoa.cpf == cpf:
            print("ENCONTRADA\n---------------------------------------")
            print("Nome:", pessoa.nome)
            print("RG:", pessoa.rg)
            print("CPF:", pessoa.cpf)
            print("----------------------------------------------")
            return
    print("Pessoa não encontrada.")
def MostrarPessoas():
    for pessoa in pessoas:
        print("----------------------------------------------")
        print("Nome: {}\nRG: {}\nCpf: {}".format(pessoa.nome, pessoa.rg,pessoa.cpf))

pessoas = []
while True:
    print("========================================")
    print("                MENU                    ")
    print("========================================")
    print("1 -  INSERIR PESSOA")
    print("2 -  CONSULTAR POR CPF")
    print("3 -  MOSTRAR TODAS AS PESSOAS")
    print("0 -  SAIR")
    print("========================================")
    opcao = int(input("ESCOLHA UMA OPÇÃO DO MENU: "))
    if opcao == 1:
        CadastrarPessoa()
    elif opcao == 2:
        PesquisaCPF()
    elif opcao == 3:
        MostrarPessoas()
    elif opcao == 0:
        print("TERMINANDO O PROGRAMA....")
        break
    else:
        print("Opção inválida, tente novamente")

