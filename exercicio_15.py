#Programa que lê e valida informações



idade = input("Digite sua idade: ")

while True:

 salario = input("Digite o valor de seu salario: ")
 sexo = input("f- feminino; m- Masculino; o- ???:     ")
 estado = input("s- Solteiro(a); c- Casado(a); v- Viuvo(a); d- Divorciado(a):    ")
 
 if idade < 0 and idade > 150:
    print("idade apenas entre 0 e 150")

salario = input("Digite o valor de seu salario: ")

while True:
    idade = input("Digite sua idade: ")
sexo = input("f- feminino; m- Masculino; o- ???:     ")
estado = input("s- Solteiro(a); c- Casado(a); v- Viuvo(a); d- Divorciado(a):    ")

if salario < 0:
    print("Permitido apenas salario maior que zero")

    sexo = input("f- feminino; m- Masculino; o- ???:     ")

    while True: 
    
        idade = input("Digite sua idade: ")
    salario = input("Digite o valor de seu salario: ")
    estado = input("s- Solteiro(a); c- Casado(a); v- Viuvo(a); d- Divorciado(a):    ")

if sexo != m and sexo != o and sexo != f:
    print("Selecio o sexo correspondente")

estado = input("s- Solteiro(a); c- Casado(a); v- Viuvo(a); d- Divorciado(a):    ")

while True: 

        idade = input("Digite sua idade: ")
salario = input("Digite o valor de seu salario: ")
sexo = input("f- feminino; m- Masculino; o- ???:     ")
 
if estado != s and estado != c and estado != v and estado != d:
    print("responda apenas s, c, v ou d. De acordo com seu estado civil")

if idade < 0 and idade < 150 and salario > 0 and sexo == f and sexo == m and sexo == o and estado == s and salario == c and salario == v and salario == d:
    print("Sucesso")