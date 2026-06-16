def estatistica():
    soma2filhos = 0
    qtd2filhos = 0
    somaSfilhos = 0
    qtdSfilhos = 0
    soma1filho = 0
    qtd1filho = 0
    somaGeral = 0
    totalPessoas = 100
    print(f"Por favor, insira os dados das {totalPessoas} pessoas:")
    for i in range(totalPessoas):
        print(f"\n Pessoa {i+1}")
        nome = input("Nome: ")
        salario = float(input("Salário:  "))
        filhos = int(input("Número de filhos: "))
        somaGeral += salario
        if filhos == 0:
            somaSfilhos += salario
            qtdSfilhos += 1
        elif filhos == 1:
            soma1filho += salario
            qtd1filho += 1
        elif filhos == 2:
            soma2filhos += salario
            qtd2filhos += 1
    
    media2f = soma2filhos / qtd2filhos if qtd2filhos > 0 else 0
    mediasf = somaSfilhos / qtdSfilhos if qtdSfilhos > 0 else 0
    media1f = soma1filho / qtd1filho if qtd1filho > 0 else 0
    mediaGeral = somaGeral / totalPessoas
    print("               RESULTADOS               ")
    print(f"a. Salário médio de funcionários com 2 filhos: R$ {media2f:.2f}")
    print(f"b. Salário médio de funcionários sem filhos: R$ {mediasf:.2f}")
    
    if media1f > media2f:
        print(f"c. A maior média é dos que têm 1 filho: R$ {media1f:.2f}")
    elif media2f > media1f:
        print(f"c. A maior média é dos que têm 2 filhos: R$ {media2f:.2f}")
    else:
        print(f"c. As médias salariais são iguais: R$ {media1f:.2f}")
    print(f"d. Salário médio geral: R$ {mediaGeral:.2f}")
estatistica()