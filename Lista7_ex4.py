carrinho = []

print("Caixa de Supermercado")
print("(Digite os valores dos produtos. 0 encerra a compra)\n")

while True:
    preco = float(input("Preço do produto: R$ "))
    if preco == 0:
        break
    carrinho.append(preco)

itens = len(carrinho)
valorBruto = sum(carrinho)
desconto = 0.0

if itens > 10:
    desconto = valorBruto * 0.05

valorFinal = valorBruto - desconto

print(f"Quantidade de itens: {itens}")
print(f"Valor Bruto: R$ {valorBruto:.2f}")
print(f"Desconto (5%): R$ {desconto:.2f}\n")
print(f"TOTAL A PAGAR: R$ {valorFinal:.2f}")
