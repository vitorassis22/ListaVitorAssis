notas = []
soma = 0
for i in range(3):
    nota = float(input("Digite a nota: "))
    notas.append(nota)
for i in range(3):
    soma += notas[i]
    media = soma/3
match media:
    case media if 0 <= media < 5:
        print("Conceito final: E")
    case media if 5 <= media < 6:
        print("Conceito final: D")
    case media if 6 <= media < 7:
        print("Conceito final: C")
    case media if 7 <= media < 8:
        print("Conceito final: B")
    case media if 8 <= media <= 10:
        print("Conceito final: A")
