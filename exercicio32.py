#Faça um programa que, dado um conjunto de N númeross, determne o menor valor, o maior valor e a soma dos valores

l = []
qnt = int(input("Digite a quantidade de elementos que deseja colocar na lista: "))
for c in range (0, qnt):
    l.append(int(input("Digite um numero: ")))
 
print ("O maior valor da lista é: ", (max(l)))
print ("O menor valor da lista é: ", (min)(l))
print ("A soma total dos valores é: ", (sum(l)))