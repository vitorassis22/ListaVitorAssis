listaA = []
listaB = []

for i in range(6):
    valorA = float(input(f"Digite um valor para lista A posição {i+1} de 6: "))
    listaA.append(valorA)
for i in range(6):
    valor_B = float(input(f"Digite o valor float para lista B posição {i+1} de 6: "))
    listaB.append(valor_B)
for i in range(6):
    listaA[i] = listaA[i] + listaB[i]

print("Lista A somada com a lista B: ")
for i in range(6):
    print(f"lista A {i+1} = {listaA[i]:.2f}")