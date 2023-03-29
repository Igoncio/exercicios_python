class Filme:
    def __init__(self, nome, duracao) -> None:
        self.nome = nome 
        self. duracao = duracao
    
    def play(self):
        print(f"{self.nome} é um filme com a duração de {self.duracao} minutos")
    
    def acao(self):
        print(f"O filme {self.nome} é de Ação\ncom explosões")
    
    def drama(self):
        print(f"O filme {self.nome}é de drama\ncom choros")

    def comedia(self):
        print(f"o filme {self.nome} é de comédia\nHAHHAHAHAHAHAHAHHAHAHHAHA")

    def suspense(self):
        print(f"O filme {self.nome} é de suspense\nMEDO")


f1 = Filme('Estrada', 180)
f1.play()
f1.acao()
print("-"* 50)
f1.drama()
print("-"* 50)
f1.comedia()
print("-"* 50)
f1.suspense()
