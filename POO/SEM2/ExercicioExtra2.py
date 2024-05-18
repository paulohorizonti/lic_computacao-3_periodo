"""
Faça um programa que contenha uma função que receba a média de um
aluno como parâmetro e retorne a situação deste aluno, conforme a tabela
abaixo
Nota Situação
< 4 R
>= 4 e < 7 EF
>= 7 A
O programa deve solicitar a média como valor de entrada para o usuário,
chamar o método e imprimir o resultado da seguinte forma:
A – Aluno Aprovado
EF – Aluno está de Exame Final
R – Aluno Reprovado
O programa deve ficar em execução até que seja digitada uma média = 0.
"""

md = float(input('DIGITE A MÉDIA DO aluno: '))

def situacaoMedia(media):
    if media < 4:
        return 'R'
    if (media >= 4) and (media < 7):
        return 'EF'
    if media >= 7:
        return 'A'

sit = situacaoMedia(md)
if sit == 'A':
    print('\033[94m A - ALUNO APROVADO \033[0m')
if sit == 'EF':
    print('\033[92m EF -ALUNO ESTÁ DE EXAME FINAL')
if sit == 'R':
    print('\033[91mR - ALUNO REPROVADO \033[0m')
