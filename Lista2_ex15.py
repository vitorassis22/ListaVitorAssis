notas = []
soma = 0
for i in range(3):
    nota = float(input("Digite a nota: "))
    notas.append(nota)
for i in range(3):
    soma += notas[i]
    media = soma/3
match media:
    case media if 0 <= media < 3:
        print("Reprovado")
    case media if 3 <= media < 7:
        print("Exame")
        nota = 12 - media
        print(f"Nota de exame necessaria: {nota}")
    case media if 7 <= media < 10:
        print("Aprovado")
