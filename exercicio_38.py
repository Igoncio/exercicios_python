#Fibonacci

n1 = 0
n2 = 1
n3 = 0

num = int(input("Digite o valor: "))
cont = 3

while cont <= num: 
    n3 = n1 + n2
    cont += 1
    n1 = n2
    n2 = n3 
    print(n3)
