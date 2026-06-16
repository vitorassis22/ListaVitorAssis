def numeroPerfeito(numero):
    if numero <= 0:
        return "Não"
    somad = 0
    for i in range(1, numero):
        if numero % i == 0:
            somad += i
    if somad == numero:
        return "Sim"
    else:
        return "Não"

resultado6 = numeroPerfeito(6)
print(f"O número 6 é perfeito? Retorno: {resultado6}") 

resultado28 = numeroPerfeito(28)
print(f"O número 28 é perfeito? Retorno: {resultado28}")

resultado25 = numeroPerfeito(25)
print(f"O número 25 é perfeito? Retorno: {resultado25}")