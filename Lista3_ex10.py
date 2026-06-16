primos = []
for n in range(2, 20001):
    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
            break
    if primo: primos.append(n)
print(f"Total de numeros primos: {len(primos)}")