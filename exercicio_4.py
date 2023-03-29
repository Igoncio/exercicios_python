#Multiplicação e casas decimais

from builtins import float, input, print


valor1 = float(input("Digie o valor1:"))
valor2 = float(input("Digite o valor2:"))
total = valor1 * valor2

print("O Total foi %.2f x %.2f foi %.2f " % (valor1, valor2, total))