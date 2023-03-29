#Programa que leia o nome de usuario e senha e não aceite a senha caso seja igual

from builtins import input, print


usuario = (input("digite um nome de usuario: "))

while True:
    senha = (input("Digite sua senha: "))

    if usuario != senha:
        print("Senha válida.")
        break
    
    elif usuario == senha:
        print("Senha repitida não é permitida")
