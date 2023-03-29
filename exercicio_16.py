


while True:
    idade = int(input("Digite sua idade: "))
    salario = float(input("Digite o valor de seu salario: "))
    sexo = input("f- feminino; m- Masculino; o- ???:     ")
    estado = input("s- Solteiro(a); c- Casado(a); v- Viuvo(a); d- Divorciado(a):    ")
 
    if (idade < 0 or idade > 150):
        print("idade permitida apenas entre 0 e 150")
        break 
