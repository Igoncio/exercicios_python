#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver contrataram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

print ("----------Reajuste de salario----------\n")
salario = float(input("Digite o salário do colaborador:"))

if salario <= 280:
    aumento1 = salario+((salario*20)/100)
    print("\n -Salario sem aumento:", salario, "\n -Percentual aplicado é de: 20%", "\n -Valor do aumento foi:",aumento1, "\n -Salario Atualizado:", aumento1)

elif salario >= 281 and salario <= 700:
    aumento2 = salario+((salario*15)/100)
    print("\n -Salario sem aumento:", salario, "\n -Percentual aplicado é de: 15%", "\n -Valor do aumento foi:",aumento2, "\n -Salario Atualizado:", aumento2)

elif salario <= 701 and salario >= 1500:
    aumento3 = salario+((salario*10)/100)
    print("\n -Salario sem aumento:", salario, "\n -Percentual aplicado é de: 10%", "\n -Valor do aumento foi:",aumento3, "\n-Salario Atualizado:", aumento3)

elif salario <=1501:
    aumento4 = salario + ((salario*5)/100)
    print("\n -Salario sem aumento:", salario, "\n -Percentual aplicado é de: 5%", "\n -Valor do aumento foi:",aumento4, "\n -Salario Atualizado:", aumento4)
