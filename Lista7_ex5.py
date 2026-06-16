votos = [1, 2, 3, 2, 2, 1, 3, 3, 2, 1, 2, 3, 2, 2, 1, 3, 2, 3, 1, 2]

ruim = 0
bom = 0
excelente = 0

for voto in votos:
    if voto == 1:
        ruim += 1
    elif voto == 2:
        bom += 1
    elif voto == 3:
        excelente += 1

total = len(votos)
porcentagemRuim = (ruim / total) * 100
porcentagemBom = (bom / total) * 100
porcentagemExcelente = (excelente / total) * 100

maiorVoto = max(ruim, bom, excelente)
porcentagemMaior = (maiorVoto/ total)
if maiorVoto == ruim:
    vencedor = "Ruim"
elif maiorVoto == bom:
    vencedor = "Bom"
else:
    vencedor = "Excelente"

print("Relatório de satisfação\n")
print(f"Ruim: {ruim} votos ({porcentagemRuim:.1f}%)")
print(f"Bom: {bom} votos ({porcentagemBom:.1f}%)")
print(f"Excelente: {excelente} votos ({porcentagemExcelente:.1f}%)")
print(f"Avaliação Vencedora: {vencedor.upper()} ({maiorVoto} votos)")
