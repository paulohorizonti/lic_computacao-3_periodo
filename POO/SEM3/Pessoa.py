class Pessoa:
    def __init__(self, nome, idade):
        self.nome  = nome
        self.idade = idade

    def saudacao(self):
        print(f"Olá, meu nome é: {self.nome} e tenho {self.idade} anos.")
pessoa1 = Pessoa("Jõao", 25)
pessoa1.saudacao()
pessoa2 = Pessoa("Maria", 28)
pessoa2.saudacao()