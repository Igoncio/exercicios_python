class Pessoa:
    def __init__(self, nome, idade, endereco) -> None:
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
    
    def get_nome(self):
        print(f"Nome: {self.nome}")
    
    def get_idade(self):
        print(f"idade: {self.idade}")

    def get_endereco(self):
        print(f"endereço: {self.endereco}")
    
    def set_idade(self, nova_idade):
        self.idade = nova_idade
    
pessoa1 = Pessoa("Igor", 17, "Tiradentes")
pessoa1.get_nome()
pessoa1.get_idade()
pessoa1.get_endereco()

pessoa1.set_idade(90)
print(f"---------\nIdade alterada para: {pessoa1.idade}")