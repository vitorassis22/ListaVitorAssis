logica = []
linguagem = []
alunos_simultaneos = []

for i in range(10):
    mat = input(f"Digite a matrícula do aluno {i+1} ou '0' para encerrar: ")
    if mat == 0:
        break
    logica.append(mat)
for i in range(8):
    mat = input(f"Digite a matrícula do aluno {i+1} ou '0' para encerrar: ")
    if mat == 0:
        break
    linguagem.append(mat)

for aluno in logica:
    if aluno in linguagem:
        alunos_simultaneos.append(aluno)

if len(alunos_simultaneos) > 0:
    print(f"Existem {alunos_simultaneos} matriculados em ambas as disciplinas")
else:
    print("Nenhum aluno está cursando as duas disciplinas ao mesmo tempo.")