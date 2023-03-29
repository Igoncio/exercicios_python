class Cachorro:
    def __init__(self, nome, raca, cor, peso, idade, porte) -> None:
        self.nome = nome 
        self.raca = raca
        self.cor = cor
        self.peso = peso
        self.idade = idade
        self.porte = porte

    def comer(self):
        print("Estou com fome AU AU")
    
    def latir(self):
        print("AU AU")
    
    def dormir(self):
        print("ZzZzZzZzZzZzZzZzZzZzZzZz")
    
    def nomes(self):
        return (self.nome)
    
    def set_nomes(self, novo):
        self.nome = novo

    def peso(self):
        return (self.peso)

    def set_peso(self, novopeso):
        self.peso = novopeso


dog1 = Cachorro("Pingo","Cofap","Caramelo",6,4,"pequeno")
dog2 = Cachorro("Roberto", "Liasa", "beje", 3, 2, "minusculo")
print(f"O nome dos cachorros são:{dog1.nomes()} e {dog2.nomes()}")
dog1.set_nomes("Gilson")
dog1.set_peso(78)
print(f"O novos dados do Cachorro são:\nNome: {dog1.nomes()}\nPeso: {dog1.peso()}")


class Gato:
    def __init__(self, nome, cor, idade, irritabilidade) -> None:
        self.nome = nome 
        self.cor = cor
        self.idade = idade
        self.irritabilidade = irritabilidade

    def coringar(self):
        print("HAHAHHAHAHAHAHAHAHA")

    def comer(self):
        print("MIAU")
     
    def dormir(self):
        print("MIAU MIAU")

    def nomes(self):
        return (self.nome)
    
gato1 = Gato("Apolo", "Branco e Preto", 3, "100%")
gato2 = Gato("James", "Branco e beje", 4, "200%")

print(f"Os nomes dos gatos são {gato1.nomes()} e {gato2.nomes()}")




        