#Um Almoxarifado controla um estoque de 5 produtos identificados pelo seu código abaixo
#Faça um programa que leia o estoque inicial de cada um dos produtos, e depois processe um certo numero de operções.
#A operação de saida do estoque deve checar se a quantidade em estoque. Se não for, exibir mensagem e impedir a operção.

cad = float(input("Digite a quantidade de caderno(s): "))
can = float(input("Digite a quantidade de caneta(s): "))
lap = float(input("Digite a quantidade de lapis: "))
bor = float(input("Digite a quantidade de borracha(s): "))
reg = float(input("Digite a quantidade de régua(s): "))

while True:
    
    print("~~~~~~~~~~ Instruções ~~~~~~~~~~")
    print("codigo                produto")
    print("                               ")
    print("10                    caderno")
    print("20                    caneta")
    print("30                    Lápis")
    print("40                    borracha")
    print("50                    Régua")
    print("                            ")
    print("E- Entrada no estoque")
    print("S- Saida no estoque")
    print("R- Relatório")
    print("X- sair")

    opção = str(input("Dígite o que deseja: "))
    
    
    if (opção == 'E'):
        cod = int(input("Digite o código do produto: "))
        if cod == 10:
            qnt = float(input("Agora digite a quantidade do produto: "))   
            cad = cad + qnt
        
        if cod == 20:
            qnt = float(input("Agora digite a quantidade do produto: "))   
            can = can + qnt

        if cod == 30:
            qnt = float(input("Agora digite a quantidade do produto: ")) 
            lap = lap + qnt
        
        if cod == 40:
            qnt = float(input("Agora digite a quantidade do produto: "))
            bor = bor + qnt
        
        if cod == 50:
            qnt = float(input("Agora digite a quantidade do produto: "))
            reg = reg + qnt
    
    if (opção == 'S'):
        cod = float(input("Digite o código do produto: ")) 
      
        
        if cod == 10:
            qnt = float(input("Agora digite a quantidade do produto: "))
            cad = cad - qnt

        if cod == 20:
            qnt = float(input("Agora digite a quantidade do produto: "))   
            can = can - qnt

        if cod == 30:
            qnt = float(input("Agora digite a quantidade do produto: "))
            lap = lap - qnt

        if cod == 40:
            qnt = float(input("Agora digite a quantidade do produto: "))
            bor = bor - qnt

        if cod == 50:
            qnt = float(input("Agora digite a quantidade do produto: "))
            reg = reg - qnt
        
        if qnt > cad and qnt > can and qnt > lap and qnt > bor and qnt > reg:
            print("Valor invalido")

    elif (opção == 'R'):

        print("A quantidade total de cadernos são: ", cad)
        print("A quantidade total de canetas são: ", can)
        print("A quantidade total de lapis são: ", lap)
        print("A quantidade total de borrachas são: ", bor)
        print("A quantidade total de reguas são: ", reg)

    else:
        opção = 'X'
        print("programa encerrado")
        break