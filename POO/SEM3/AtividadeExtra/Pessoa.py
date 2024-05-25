"""Implementar um programa com a classe Pessoa, que contém os atributos
nome, idade e peso; que contém os métodos individuais para atribuir nome
(set_nome(nome)), idade(set_idade(idade)) e peso (set_peso)) e um método
para mostrar todos os dados (mostrarDados()). O método construtor deve ser
implementado."""
class Pessoa:
    def set_nome(self, nome):
        self.nome = nome
    def set_idade(self, idade):
        self.idade = idade

    def set_peso(self, peso):
        self.peso = peso

    def MostrarDados(self):
        print("Nome: {}\nIdade: {}\nPeso: {}".format(self.nome, self.idade, self.peso))
pessoa1 = Pessoa()
pessoa1.set_nome("PEDRO")
pessoa1.set_idade(44)
pessoa1.set_peso(85)
pessoa1.MostrarDados()