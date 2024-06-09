class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def get_nome(self):
        return self.__nome

pessoa1 = Pessoa("Paulo",19)
print(pessoa1.__idade)
