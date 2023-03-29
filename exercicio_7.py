#Programa que lê os valores em reais e transforma em dólares

from builtins import float, input, print


reais = float(input("Digite a quantia dos reais:"))
cot = float(input("Digite o valor da cotação:"))
dolar = reais * cot

print("o valor do dólar equivale a:", cot )
print("\nO total do real transformado em dólar é:", dolar)