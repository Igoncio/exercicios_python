lista = []
i = int(input("Digite a quantidade de numeros a serem digitados: "))
for args in range (1, i+1):
    args = float(input(f"Digite o {args}° numero:"))
    lista.append(args)

def função (media, remov ,*args):

    remov = lista.remove[0]
    qnt = len(lista)
    media = sum(lista)/qnt
    return media, remov, qnt
media = args
print(f"A Média é {args}")