class Automovel:
    def __init__(self, marca, modelo, ano, ligado=False):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = ligado

    def Ligar(self):
        self.ligado = True
    def Desligar(self):
        self.ligado = False

    def Mostrar(self):
        print("Marca: {}\nModelo: {}\nAno: {}\nLigado? : {}".format(self.marca, self.modelo, self.ano, self.ligado))

carro1 = Automovel("Fiat", "Palio", "2010")
carro1.Desligar()
carro1.Mostrar()
print("-------------------------------------------------")
carro2 = Automovel("Ford","Fiesta","2008")
carro2.Ligar()
carro2.Mostrar()