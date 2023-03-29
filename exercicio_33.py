#Faça um programa que peça para N pessoas a sua idade, ao final o programa devera verificar se a media da idade da turma varia entre 0 e 25,
# 26 e 60 e maior que 60; e entao, dizer se a turma é jovem, adulta ou idosa, confor,e a média calculada.
jovem = 0; adulto = 0; velho_lixo = 0
maior = []
nomes = ["jovem", "adulta", "velho_lixo"]
qnt = int(input("Digite o numero de alunos:  "))
for x in range (0, qnt):
    x = int(input("Qual sua idade ?"))
    if (x>=0 and x<=26):
        jovem = jovem + 1
    elif (x>= 26 and x<=60):
        adulto = adulto + 1
    else:
        velho_lixo = velho_lixo + 1
maior.append(jovem)
maior.append(adulto)
maior.append(velho_lixo)
for b in range (len(maior)):
    if (max(maior)==maior[b]):
        print ("sua sala é", nomes[b])
