num_funcionario = 0; valor_gasto = 0; recebe_minimo = 0; abono_total = 0; salarioss = []; salario_min = 1300; abonos = []; abono_min = 100; qnt_salario = []; qnt_salarioT = 0

print("---------- Abono Salarial ----------")

while True:
    entrar = int(input("\n Digite 1 para continuar ou 0 para encerrar (caso digite zero no campo salarial o programa ira encerrar):\n -->"))
    num_funcionario = num_funcionario + entrar
    if entrar == 1:
        qnt = int(input("Digite a quantidade de funcionarios:"))

        for i in range (1, qnt+1):
            salario = float(input(f"Digite o valor do {i}° salario:"))
            qnt_salarioT = qnt_salarioT + 1
            qnt_salario.append(qnt_salarioT)
            if salario == salario_min:
                salariomin = salario + abono_min
                recebe_minimo = recebe_minimo + 1
                salarioss.append(salariomin)
                abonos.append(abono_min)

            if salario > salario_min:
                abono_maior = (salario*20)/100
                salario = salario + abono_maior
                salarioss.append(salario)
                abonos.append(abono_maior)
                
    elif entrar == 0:

        print("---------Salarios----------")
        print(*salarioss, sep="\n")
        print("-------- Abonos --------")
        print(*abonos, sep="\n")
        print(f"O total de funcionário foi de --> {qnt}")
        print(f"O total de funcionario que receberam apenas 100 reais de abono foram -->{recebe_minimo}")
        print(f"O maior valor do abono foi de {max(abonos)}")
        print(f"O valor gasto com abonos foi de {sum(abonos)}")
        break
