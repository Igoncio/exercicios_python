class Agenda:
    def __init__(self, dia= None, mes= None, ano= None, anotacao= None) -> None:
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anotacao = anotacao

    def dia(self, dia):
        return dia 

    def mes(self, mes):
        return mes 
    
    def ano(self, ano):
        return ano 
    
    def anotacao(self, anotacao):
        return anotacao 
 
while True:
    info1 = Agenda()
    dia = int(input("Digite o dia do mês da sua anotação: "))
    mes = int(input("Digite o mes da sua anotação: ")) 
    ano = int(input("Digite o ano da sua anotação: "))
    anotacao = input("Digite o que deseja anotar: ")

    if dia > 31:
        print("Dia não valido")
        break

    if mes > 12:
        print("Mês não valido")
        break

    if ano > 2023:
        print(f"Ainda falta(m) {ano - 2023} anos para validar sua anotação")
        break        

    ver_anotação = int(input("\nDigite 1 para ver suas anotações: "))

    if ver_anotação == 1 and mes == 1:
        print(f"\nDia --> {dia}")
        print(f"Mês --> Janeiro ({mes})")
        print(f"Ano --> {ano}")
        print(f"Anotação--> {anotacao}")
    
    if ver_anotação == 1 and mes == 2:
        print(f"\nDia --> {dia}")
        print(f"Mês --> Fevereiro ({mes})")
        print(f"Ano --> {ano}")
        print(f"Anotação--> {anotacao}")
    
    if ver_anotação == 1 and mes == 3:
        print(f"\nDia --> {dia}")
        print(f"Mês --> Março ({mes})")
        print(f"Ano --> {ano}")
        print(f"Anotação--> {anotacao}")
        
        
