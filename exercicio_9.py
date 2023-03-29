#Programa que da opção para selecionar o turno escolhido e imprime "bom dia"; "boa tarde"; "boa noite" de acordo com o turno selecionado

from builtins import input, print, str


print("-----Selecione o turno em que você estuda-----\n")
turno = str(input("Escolha a letra de acordo com o seu turno:\n M- para Matutino\n V- para Vespertino\n N- para Noturno\n Digite aqui:"))
if (turno == 'M'):
    print("Bom dia")

elif (turno == 'V'):
    print("Boa Tarde")

elif (turno == 'N'):
    print("Boa Noite")

else:
    print("Valor invalido")
