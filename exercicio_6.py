#Programa que lê o nome do produto, a quantidade comprada, o valor unitario e o percentual de desconto a ser aplicado para o pagamento.

nm = str(input("Digite o nome do Produto:"))
qp = float(input("Digite a quantia de produtos comprados:"))
vu = float(input("Agora digite o valor unitario do produto:"))
pg = float(input("Indique a quantidade de desconto que devera ser aplicado ao produto:"))

total = vu * qp
desconto = total * pg / 100

print("O nome do produto é:", nm, "\nA qauntidade de produtos é:", qp, "\nO valor do produto é:", vu, "\nA quantia total com o desconto aplicado é:", desconto)