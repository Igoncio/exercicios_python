#Numa eleicão existem 3 candidatos. Faça um programa que peça o numero total de eleitores. Peça para cada eleitor votar e ao final mostrar o 
#numero de votos de cada candidato

th = 0
rob = 0
vini = 0
cont = 0
print("~~~~~~~~~~ CANDIDATOS ~~~~~~~~~~")
print("1- Thiago Leifer")
print("2- Roberto Carlos")
print("3- Vinicius Martins")

eleitor = int(input("Digite o numero de eleitores: "))
for c in range (0, eleitor):
    voto = int(input("Digite seu voto-->"))
    if voto == 1:
        th = th+1
        print("voto para Thiago")

    if voto == 2:
        rob = rob+1
        print("Voto para Roberto")

    if voto == 3:
        vini = vini+1
        print("Voto para Vinicius")

else:
    print("--------------------------")
    print(th, "Votos para thiago")
    print(rob, "Votos para Roberto")
    print(vini, "Votos para Vinicius")
 
