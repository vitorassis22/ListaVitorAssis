listaA = []

for i in range(8):
    valor = int(input(f"Numero {i+1}: "))
    listaA.append(valor)
maior = listaA[0]
for i in range(1, len(listaA)):
    if listaA[i] > maior:
        maior = listaA[i]
print(f"O maior valor encontrado na lista é: {maior}")