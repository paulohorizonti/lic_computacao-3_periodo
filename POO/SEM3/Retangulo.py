class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def area(self):
        return self.altura * self.largura
retangulo1 = Retangulo(5,10)
print(retangulo1.area())

retangulo2 = Retangulo(5.5,10)
print(retangulo2.area())