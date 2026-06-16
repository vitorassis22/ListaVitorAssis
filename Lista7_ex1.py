nomes = []
medias = []

print("Cadastro de alunos")
for i in range(5):
    nome = input(f"\nDigite o nome do {i+1}º aluno: ")
    media = float(input(f"\nDigite a média final do {nome}: "))
    nomes.append(nome)
    medias.append(media)

soma = sum(medias)
media = soma / 5

print(f"\nMÉDIA GERAL DA TURMA: {media:.2f}")
print("Boletim dos Alunos:")

acimaMedia = 0
for i in range(5):
    print(f" - {nomes[i]}: Nota {medias[i]:.1f}")
    if medias[i] > media:
        acimaMedia += 1
print(f"Alunos acima da média geral: {acimaMedia}")
