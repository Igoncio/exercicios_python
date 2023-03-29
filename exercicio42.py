#Um restaurante que enfrenta problemas com sua capacidade de cliente pediu sua ajuda para fazer um programa para saber quando eles atingem sua capacidade maxima.

cont = 0
print("{:-^50}".format("RESTAURANTE"))
print("1- Para continuar")
entrar = int(input("Deseja continuar -->"))
cap = int(input("Digite a capacidade maxima:"))
while True:
    if entrar == 1:
        adc = int(input("\nDigite 2 para adicionar um cliente: "))
    if adc == 2:
        cont = cont + 1
        print(cont, "clientes")
    if cont > cap or cont == cap:
        print("<<Capacidade maxima atingida>>")
        break