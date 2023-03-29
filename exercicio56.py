class Aluno:
    def __init__(self, nome, ra, *args) -> None:
        self.nome = nome
        self.ra = ra
        self.args = args
    
    def get_nome(self):
        print(f"Nome: {self.nome}")

    def get_ra(self):
        print(f"Ra: {self.ra}")

    def get_sum(self):
        soma = sum(self.args)
        self.args = soma


nota1 = Aluno("Robertinho", "14945", 8, 8, 5, 5)
nota1.get_nome()
nota1.get_ra()
print(f"As 4 notas foram: {nota1.args}")
soma = sum(nota1.args)/4
print(f"A média das notas é: {soma}")

if soma >= 7:
    print("Aprovado")

if soma < 6.9 and soma > 5:
    print("Exame")

if soma < 5:
    print("Reprovado")

