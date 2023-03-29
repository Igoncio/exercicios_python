class Ingresso:
    def __init__(self, preco, setor) -> None:
        self.preco = preco
        self.setor = setor
        
    
    def alterar_preco(self):
        alt = input("Digite o valor desejado para alterar o valor do preço: ")
        print(f"O valor antigo era: {self.preco}\nNovo Valor: {alt}")
        return alt
      
    def  mostrar_setor(self):
        print(f"Setor: {self.setor}")   

class IngressoVip(Ingresso):
    def __init__(self, camarote, open_bar, open_food, estacionamento, preco, setor) -> None:
        super().__init__(preco, setor)
        
        self.camarote = camarote
        self.open_food = open_food
        self.open_bar = open_bar
        self.estacionamento = estacionamento     
    
    
    def boleano(self):
                
        vip_ou_nao = input("Ingresso VIP S/N?").upper()
    
        if vip_ou_nao == 'S':
            print(f"CAMAROTE: {self.camarote}")
            print(f"OPEN FOOD: {self.open_food}")
            print(f"OPEN BAR: {self.open_bar}")
            print(f"ESTACIONAMENTO: {self.estacionamento}")
            
        else:       
            print(f"CAMAROTE: NÃO")
            print(f"OPEN FOOD: NÃO")
            print(f"OPEN BAR: NÃO")
            print(f"ESTACIONAMENTO: NÃO")       
        
if __name__ == '__main__':
    i = Ingresso(900, 'vendas')
i.alterar_preco()
i.mostrar_setor()
print("="*90)
i2 = IngressoVip('OK', 'OK', 'OK', 'OK', 'Norte', 50)
i2.boleano()