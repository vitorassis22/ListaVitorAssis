def numeros():
    qtd = 100
    somaPositivos = 0
    qtdPositivos = 0
    somaNegativos = 0
    qtdNegativos = 0
    print("Digite 100 numeros inteiros: ")
    for i in range(qtd):
        num = int(input(f"Numero {i+1}: "))
        if num > 0:
            qtdPositivos += 1
            somaPositivos += num
        else: 
            qtdNegativos += 1
            somaNegativos += num
    if qtdPositivos > 0:
        mediaPositivos = somaPositivos / qtdPositivos
    else: print("Nao existem numeros positivos")
    if qtdNegativos > 0:
        mediaNegativos = somaNegativos / qtdNegativos
    else: print("Nao existem numeros negativos")
    print(f"A soma dos números positivos foi: {somaPositivos}")
    print(f"A média de números positivos foi: {mediaPositivos:.2f}")
    print(f"A soma dos números negativos foi: {somaNegativos}")
    print(f"A média de números negativos foi: {mediaNegativos:.2f}")
    diferenca = qtdPositivos - qtdNegativos
    if diferenca > 0:
        print(f"A diferença entra positivos e negativos foi: {diferenca}")
    else: print(f"A diferença entra negativos e positivos foi: {abs(diferenca)}")