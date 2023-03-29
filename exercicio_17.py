while True:
    print("|==================================INSTRUÇÕES===================================|")
    print("|                1°- sua idade deve ser entre 1 e 150                           |")
    print("|                2°- seu salário deve ser maior que 0                           |")
    print("|3°- para seu sexo digite F para feminino, M para masculino e O para outros     |")
    print("|4°- Digite S se for solteiro, C para casado, V para viúvo(a) ou D para divórcio|")
    print("|           5°- Digite 1 para começar e 'sair' para fechar o programa           |")
    print("|===============================================================================|")

    entrar=int(input())
    if entrar==1:
        
        while True:
            idade=float(input("Digite sua idade:"))
            if (idade>=0 and idade<=150):
                print("idade cadastrada")
                print("---------------------")
                break
            else:
                print ("Idade inválida")
                
        while True:    
            sal=float(input("Digite o seu salário: "))
            if (sal>0):
                print("salário cadastrado")
                print("---------------------")
                break
                
            else:
                print ("Valores inválidos")

        while True:
            sexo=input("Digite o seu sexo: ")
            if sexo=='f':
                print("sexo cadastrado (feminino)")
                print("---------------------")
                break
            elif sexo=='m':
                print("sexo cadastrado (masculino)")
                print("---------------------")
                break
            elif sexo=='o':
                print("sexo cadastrado (outros)")
                print("---------------------")
                break
            else:
                print("Sexo inválido")
        
        while True:
            ec=input("Digite seu estado civil: ")
            if ec=='s':
                print("Estado civil cadastrado (solteiro)")
                print("---------------------")
                break
            elif ec=='c':
                print("Estado civil cadastrado (casado)")
                print("---------------------")
                break
            elif ec=='v':
                print("Estado civil cadastrado (Viúvo)")
                print("---------------------")
                break
            elif ec=='d':
                print ("Estado civil cadastrado (Divorciado)")
                print("---------------------")
                break
            else:
                print("Estado Civil inválido")

    elif entrar!=1:
        break