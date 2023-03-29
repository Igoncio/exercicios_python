class Pessoa:
    def __init__(self, nome, matricula, idade) -> None:
        self.nome = nome
        self.matricula = matricula
        self.idade = idade
    
class Aluno(Pessoa):
    def __init__(self, nome, matricula, idade, nota, nota2, nota3, nota4) -> None:
        super().__init__(nome, matricula, idade)
        self.nota = nota
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
        self.media = 0

    def calcular_media(self):
        media = ( self.nota + self.nota2 + self.nota3 + self.nota4 ) / 4
        return media
        
    def estudar(self):
        print(f"{self.nome} deve estudar TODAS as materias")
        
    def lecionar(self):
        print(f"{self.nome} não serve para lecionar")

class Professor(Pessoa):
    def __init__(self, nome, matricula, idade, salario, carga_horaria, formacao, diciplina) -> None:
        super().__init__(nome, matricula, idade)
        self.salario = salario
        self.carga_horaria = carga_horaria
        self.formacao = formacao
        self.diciplina = diciplina
    
    def info(self):
        print(f"{self.nome} é professor de: {self.diciplina}\nSua formação é: {self.formacao}\nCarga horaria de {self.carga_horaria} horas\nSalario{self.salario}")
        
        
if __name__ == "__main__":
    a1 = Aluno('Igor',323232, 17, 4, 4, 4, 4)
print(a1.calcular_media())
a1.estudar()
a1.lecionar()
print("-"*90)
p1 = Professor('Emanoel', 5645734537, 99,90000, 8, 'Matematica', 'Fisica' )
p1.info()
