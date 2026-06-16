numeros = []
print("Digite 8 números inteiros:")
for i in range(8):
    num = int(input(f"Número {i+1}: "))
    numeros.append(num)
multiplos2 = []
multiplos3 = []
for num in numeros:
    if num % 2 == 0:
        multiplos2.append(num)
    if num % 3 == 0:
        multiplos3.append(num)
print(f"Números múltiplos de dois: {multiplos2}")
print(f"Números múltiplos de três: {multiplos3}")