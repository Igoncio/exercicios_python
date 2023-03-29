#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja invalido e continue pedindo até que o usuario informe um valor valido.

from builtins import float, input, print


while True:
    valor = float(input("Digite um valor entre zero e dez: "))
    if valor <= 0 and valor <= 10:
        print("Valor válido")

    if valor > 0 and valor > 10:
        print("valor invalido")
        break
        




