maior = 0
for i in range(5):
    n = int(input("Insira um numero: "))
    if n > 100:
        maior += 1
print(f"Foram digitados {maior} numeros maiores que 100")
