gabarito = []
aluno = []
resposta_aluno = []
maior = 0
menor = 9999999999999999
nome_menor = ''
nome_maior = ''
qnt_nome = 0
total = 0
for c in range(1,11):
    professor = input(f"Resposta da questão {c}°:")
    gabarito.append(professor)

while True:
    op = int(input("Digite 1 para continuar ou 0 para sair \n"))
    if op == 1:
        nome = (input("Digite seu nome: "))
        qnt_nome = qnt_nome + 1
        acerto = 0
        cont = 0
        for c in gabarito:
            cont = cont+1
            resp = input(f"Digite a resposta da questão {cont}:")
            if c == resp:
                acerto = acerto + 1
        total = total + acerto
            
        print(f"{nome} teve um quantidade de {acerto} \n")

    if maior < acerto:
        maior = acerto
        nome_maior = nome
    
    if menor < acerto:
        menor = acerto
        nome_menor = nome

    elif op == 0:
        
        media = total/qnt_nome
        print("------------------------------------------------------------------")
        print(f"{nome} teve menos acertos com apenas {acerto} respostas corretas")
        print(f"{nome_maior} teve mais acertos com {maior} acertos")
        print(f"{qnt_nome} alunos responderam o gabarito")
        print(f"A média da nota dos alunos é {media}")
        break