n = int(input("Insira um numero: "))
if n < 0:
    print("Insira um numero positivo") 
f = 1
for i in range(1, n + 1):
    f *= i  
print(f"O numero {n} fatorial é {f}")