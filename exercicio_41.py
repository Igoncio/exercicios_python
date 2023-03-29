#Programa para instituição de doação de sangue

print("---------- INSTRUÇOES ----------")
print("1- Para continuar")
entrar = int(input("Deseja continuar -->"))
while True:
    if entrar == 1:
        idade = float(input("Digite sua idade(entre 16 a 69 anos):"))
        peso = float(input("Digite seu peso(mais de 50kg):"))
        neca = float(input("Digite a quantidade de tempo dormido nas ultimas 24 horas (pelo menos 6 horas)"))
    if idade > 69 or idade < 16:
        print("Não apto a doar sangue \n motivo: idade invalida")
    if peso < 50:
        print("Não apto a doar sangue. \n motivo: Peso irregular")
    if neca < 6:
        print("Não apto a doar sangue. \n motivo: Sono irregular")
    else: 
        print("Apto a doar sangue")
        break
