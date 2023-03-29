#Faça um programa que calcule o fatorial de um numero inteiro fornecido pelo usuario:

valor = int(input("Digite um valor: "))
v = 1

for c in  range (valor , 1, -1):
    v = v * c
print("o resultado do fatorial é:", v)
