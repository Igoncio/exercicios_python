class Banco:
    def __init__(self,nome,cpf,num,saldo) -> None:
        self.nome = nome
        self.cpf = cpf
        self.num = num
        self.saldo = saldo

    def get_nome(self):
        print(f"Nome: {self.nome}")

    def get_cpf(self):
        print(f"Cpf: {self.cpf}")

    def get_num(self):
        print(f"Numero: {self.num}")

    def get_saldo(self):
        print(f"Saldo: {self.saldo}")
    
    def set_saldo(self,now):
        self.saldo = now

ss = 50
banco = Banco("Vinicius","661.520.547.47",992556873,ss)
banco.get_nome()
banco.get_cpf()
banco.get_num()
banco.get_saldo()
print("Só é possivel realizar um saque se o saldo for POSITIVO!")
while True:
    now = int(input("Digite 1 para Deposito, 2 para Saque ou 0 para sair: "))
    if now == 1:
        dep = float(input("Digite o valor do deposito: "))
        ss = ss+dep
        print(f"Saldo: {ss}")

    elif now == 2:
        saq = float(input("Digite o valor do saque: "))
        ss = ss-saq
        if saq > ss:
            print("Saldo Negativo")
            break
        print(f"Saldo: {ss}")
    else:
        now == 0
        print("Operação Encerrada")
        break

