"""
Faça um programa que efetue o cálculo do reajuste do salário de 15
funcionários. Considere que cada funcionário deverá receber um reajuste de
15%, caso seu salário seja menor que 500. Caso contrário, o reajuste deverá ser
de 5%. O cálculo do reajuste deverá ser realizado em uma função chamada
calcularReajuste(), que recebe como parâmetro os salários atuais e retorna
uma lista com os novos salários.
Considere que:
- o salários atuais deverão ser armazenados em uma lista ‘Salario’, que será
passado por parâmetro para a função calcularReajustes();
- os nomes dos funcionários deverão ser armazenados em uma lista
‘Nomes’, que será passada para a função calcularReajustes();
- os novos salários deverão ser armazenados em uma lista chamada
NovoSalario, que será preenchida na função correspondente
- Imprima, para cada funcionário, o nome, o salário atual e o novo salário.
* Assuma que cada índice da lista corresponde a um funcionário.
"""
def calculaReajustes(salarios):
    novoSalario = []
    for i in range(len(salarios)):
        if salarios[i]>500:
            novoSalario.append(salarios[i]+((salarios[i]*15)/100))
        if salarios[i]<=500:
            novoSalario.append(salarios[i] + ((salarios[i] * 5) / 100))
    return novoSalario

def criarListas():
    salarios = []
    nomes = []

    for i in range(0,2):
        nomes.append(input('DIGITE O NOME DO FUNCIONÁRIO: ').upper())
        salarios.append(float(input('DIGITE O SALARIO DESSE FUNCIONARIO: ')))

    novosalario = calculaReajustes(salarios)
    print('------------------------------------------')
    print('NOME\t|\tSALÁRIO\t|\tNovo Salário')
    print('------------------------------------------')
    for i in range(len(nomes)):
        print(nomes[i],"\t|\t",salarios[i],'\t|\t',novosalario[i] )
    print('------------------------------------------')

criarListas()