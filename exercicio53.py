class Automovel:
    def __init__(self, cor,  placa ="HSB-9999") -> None:
        self.cor = cor
        self.placa = placa

    def dirigir(self, velocidade):
        print(f"Estou dirigindo a {velocidade}")
    
    def get_placa(self):
        print(self.placa)
    
    def get_cor(self):
        print(self.cor)

car1 = Automovel("Prata")
car1.get_placa()
car1.get_cor()
car1.dirigir(68)

print("---------------------------------------------------------------------------------")

class Carro:
    def __init__(self, roda, bodykit, cor) -> None:
        self.roda = roda
        self.bodykit = bodykit
        self.cor = cor

    def get_roda(self):
        print(self.roda)
    
    def get_bodykit(self):
        print(self.bodykit)

    def get_cor(self):
        print(self.cor)

car2 = Carro("Roda Libert Walk","Sem body Kit", "Cor Azul")
car2.get_bodykit()
car2.get_roda()
car2.get_cor()

