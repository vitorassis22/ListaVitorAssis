impar = 0
par = 0
num = 0
n = int(input("Insira o tamanho da sequencia: "))
for i in range(n):
    num += 1
    if n > 0:
        if num % 2 == 0:
            par += 1
        else: impar += 1
    else: print("Insira um valor positivo")
print(f"Na sequencia existem {par} pares e {impar} impares")