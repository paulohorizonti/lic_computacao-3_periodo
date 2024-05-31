class Automovel:
    def __init__(self, marca, modelo, ano, ligado=False):
        self.marca = marca
        self.modelo=modelo
        self.ano=ano
        self.ligado=ligado
    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def mostrar(self):
        print(f"{self.marca}, {self.modelo}, {self.ano}, {self.ligado}")

automovel1 = Automovel("Fiat","Palio",2022)
print(automovel1.mostrar())

