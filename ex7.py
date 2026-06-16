def sequencia():
    soma = 0
    qtd = 0
    maior = 0
    menor = 0
    
    while True:
        num = float(input("Digite um número: "))
        soma += num
        qtd += 1
        
        if maior == 0 or num > maior:
            maior = num
        if menor == 0 or num < menor:
            menor = num
            
        continuar = input("Deseja continuar? (S/N): ")
        if continuar == 'N' or continuar == 'n':
            break
    if qtd > 0:
        media = soma / qtd
        print(f"Media: {media:.2f}")
        print(f"Maior número: {maior}")
        print(f"Menor número: {menor}")
    else:
        print("Nenhum número foi inserido.")
sequencia()