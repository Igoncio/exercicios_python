saltos = []; nome = []; medias = []

while True:
    entrar = int(input("\n Digite 1 para continuar ou 0 para sair\n -->"))
    if entrar == 1:
        dig_nome = input("\n Digite seu nome:")
        nome.append(dig_nome)
        for c in range (1, 6):
            salto = float(input(f"{c}° Salto: "))
            saltos.append(salto)
            maior = max(saltos); menor = min(saltos)
        
        print (f"\n Melhor salto: {maior}")
        print(f"Pior Salto: {menor}")
        saltos.remove(maior); saltos.remove(menor)
        media = sum(saltos)/3
        print(f"A média dos demais saltos é: {media}") 
        medias.append(media)     
        saltos.clear()
        medias.sort()
       
    elif entrar == 0:
        print(f"1° lugar:{medias[-1]}")
        print(f"2° lugar:{medias[-2]}")
        print(f"3° lugar:{medias[-3]}")
        
        break
