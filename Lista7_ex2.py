movimentacoes = []

print("Registro de Movimentações Diárias")
print("Valores positivos = Vendas | Valores negativos = Despesas | 0 = Sair\n")

while True:
    valor = float(input("Digite o valor da movimentação: R$ "))
    if valor == 0:
        break
    movimentacoes.append(valor)

total = 0
totalGasto = 0

for mov in movimentacoes:
    if mov > 0:
        total += mov
    else:
        totalGasto += mov

saldoFinal = total + totalGasto

print("RELATÓRIO FINANCEIRO")
print(f"Total Arrecadado: R$ {total:.2f}")
print(f"Total Gasto: R$ {abs(totalGasto):.2f}")
print(f"Saldo Final: R$ {saldoFinal:.2f}")

if saldoFinal > 0:
    print("\nSituação: LUCRO")
elif saldoFinal < 0:
    print("\nSituação: PREJUÍZO")
else:
    print("\nSituação: NEUTRO")