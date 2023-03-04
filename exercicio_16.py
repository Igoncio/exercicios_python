#Um Almoxarifado controla um estoque de 5 produtos identificados pelo seu código abaixo
#Faça um programa que leia o estoque inicial de cada um dos produtos, e depois processe um certo numero de operções.

caneta = int(input("Digite a quantidade de CANETAS no estoque: ")) 
caderno = int(input("Digite a quantidade de CADERNOS no estoque: "))
lapis = int(input("Digite a quantidade de LAPIS no estoque: ")) 
borracha = int(input("Digite a quantidade de BORRACHAS no estoque: "))
regua = int(input("Digite a quantidade de REGUAS no estoque: "))
print("------------Tabela de Produtos---------------------------")
print("10                   caderno\n20                   caneta")
print("30                   lapis\n40                   borracha")
print("50                   regua")
print("---------------------------------------------------------")
print("obs: NÃO ESQUEÇA DE COLOCAR PELO MENOS UMA QUANTIDADE (nem que seja ZERO) PARA CADA PRODUTO")
while True:
    print("E - entrada no estoque\nS - Saída do estoque\nR - Relatório\nX - Sair")
    opção = input("Digite sua escolha\n-->")

    if opção == 'E':

        codigo = int(input("Digite o codigo do produto que queira adicionar: "))
        quantidade = int(input("Digite a quantidade desse produto: "))

        if codigo == 10:
            e_caderno = caderno + quantidade
            print(f"\n{e_caderno} Cadernos adicionados\n-----------------------------------")
        
        if codigo == 20:
            e_lapis = lapis + quantidade
            print(f"\n{e_lapis} Lapis adicionados\n-----------------------------------")
        
        if codigo == 30:
            e_caneta = caneta + quantidade
            print(f"\n{e_caneta} Lapis adicionados\n-----------------------------------")
        
        if codigo == 40:
            e_borracha = borracha + quantidade
            print(f"\n{e_borracha} Lapis adicionados\n-----------------------------------")
        
        if codigo == 50:
            e_regua = regua + quantidade
            print(f"\n{e_regua} Lapis adicionados\n-----------------------------------")
    
    if opção == 'S':

        codigo = int(input("Digite o codigo do produto que queira dar saida: "))
        quantidade = int(input("Digite a quantidade desse produto: "))

        if codigo == 10:
            s_caderno = caderno - quantidade
            print(f"\n{s_caderno} Cadernos no estoque\n-----------------------------------")
        
        if codigo == 20:
            s_lapis = lapis - quantidade
            print(f"\n{s_lapis} Lapis no estoque\n-----------------------------------")
        
        if codigo == 30:
            s_caneta = caneta - quantidade
            print(f"\n{s_caneta} Lapis no estoque\n-----------------------------------")
        
        if codigo == 40:
            s_borracha = borracha - quantidade
            print(f"\n{s_borracha} Lapis no estoque\n-----------------------------------")
        
        if codigo == 50:
            s_regua = regua - quantidade
            print(f"\n{s_regua} Lapis no estoque\n-----------------------------------")

            t_caderno = e_caderno + s_caderno
            t_lapis = e_lapis + s_lapis
            t_caneta = e_caneta + s_caneta
            t_borracha = e_borracha + s_borracha
            t_regua = e_regua + s_regua    
    if opção == 'R':
        
        print(f"-----------RELATORIO-----------\n{t_caderno} Caderno(s)\n{t_lapis} lapis(s)\n{t_caneta} caneta(s)\n{t_borracha} borracha(s)\n{t_regua} regua(s)")
    
    if opção == 'X':
        print("Programa encerrado :)")
    break
