numeros = []
print("Digite 6 números inteiros:")
for i in range(6):
    num = int(input(f"Número {i+1}: "))
    numeros.append(num)
pares = []
impares = []
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print(f"Quantidade de pares: {len(pares)}")
print(f"Números pares: {pares}")
print(f"Quantidade de ímpares: {len(impares)}")
print(f"Números ímpares: {impares}")