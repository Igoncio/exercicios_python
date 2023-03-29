#foi feita uma estatistica em cinco cidades brasileiras para coletar dados sobre acidentes de transito. Foram obtidos os seguintes dados:
#Código da cidade;
#Numeros de veiculos de passeio (em 1999);
#Numero de acidentes de transito com vitimas (em 1999);
#deseja-se saber:
#Qual o maior e menor indice de acidentes de transito e a que cidade pertence;
#Qual a media de veiculos nas cinco cidades juntas;
#Qual a media de acidentes de transito nas cidades com menos de 2000 veículos de passeio
lista_ac = []
listav = []
print("---------- Estatistica ----------")
print("1- Para primeira cidade")
print("2- Para segunda cidade")
print("3- para terceira cidade")
print("4- para quarta cidade")
print("5- para quinta cidade")

for c in range (1,6):
    cod = int(input("Digite o código da cidade:"))
    if cod == 1:
        n_v1 = int(input("Digite o numéros de veiculos de passeio: "))
        n_a1 = int(input("Digite o numero de acidentes: "))
        print("\n")

    elif cod == 2:
        n_v2 = int(input("Digite o numéros de veiculos de passeio: "))
        n_a2 = int(input("Digite o numero de acidentes: "))
        print("\n")

    elif cod == 3:
        n_v3 = int(input("Digite o numéros de veiculos de passeio: "))
        n_a3 = int(input("Digite o numero de acidentes: "))
        print("\n")

    elif cod == 4:
        n_v4 = int(input("Digite o numéros de veiculos de passeio: "))
        n_a4 = int(input("Digite o numero de acidentes: "))
        print("\n")

    elif cod == 5:
        n_v5 = int(input("Digite o numéros de veiculos de passeio: "))
        n_a5 = int(input("Digite o numero de acidentes: "))
        print("--------------------------------------------------------------------------------------------")

        listav.append(n_v1); listav.append(n_v2); listav.append(n_v3); listav.append(n_v4); listav.append(n_v5)
        lista_ac.append(n_a1); lista_ac.append(n_a2); lista_ac.append(n_a3); lista_ac.append(n_a4); lista_ac.append(n_a5)
        media_veiculo = (sum(listav)) / 5
        
        print("O maior indice é: ", max(lista_ac))
        print("O menor indice é: ", min(lista_ac))
        print(f"A média de veiculos das 5 cidades é: {media_veiculo}")
