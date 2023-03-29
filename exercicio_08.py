#Programa que faz a leitura de 3 alagritimos e os-escreve em ordem decrescente

from builtins import float, input, print


num1 = float(input("Digite o primeiro numero:"))
num2 = float(input("Digite o segundo numero:"))
num3 = float(input("Digite o terceiro numero:"))

if num1 > num2 and num1 > num3 and num3 > num2: 
    print(num1, num3, num2)

if num1 > num2 and num1 > num3 and num2 > num3:
    print(num1, num2, num3)

if num2 > num1 and num2 > num3 and num3 > num1:
    print(num2, num3, num1)

if num2 > num1 and num2 > num3 and num1 > num3:
    print(num2, num1, num3)

if num3 > num1 and num3 > num2 and num1 > num2:
    print(num3, num1, num2)

if num3 > num1 and num3 > num2 and num2 > num1:
    print(num3, num2, num1)
