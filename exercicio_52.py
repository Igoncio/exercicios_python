class Computador:
    def __init__(self, marca, modelo, proc, ram, ssd, preco) -> None:
        self.marca = marca
        self.modelo = modelo
        self.proc = proc
        self.memoria = ram
        self.hd = ssd
        self.valor = preco

    def get_marca(self):
        return self.marca

    def get_preco(self):
        return self.valor
    
    def set_preco(self, novo_preco):
        self.valor = novo_preco
    
comp1 = Computador("Asus", "Note2023", "Core i5", "12GB", "1TB SSD", 3600)
print ("Preço atual:",comp1.get_preco())
comp1.set_preco(2900)

print ("Preço atual 2:",comp1.get_preco())
    
