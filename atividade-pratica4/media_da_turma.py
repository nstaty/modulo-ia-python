# Média da Turma

qtd_alunos = int(input("Digite a quantidade de alunos: "))
notas = []

for i in range(qtd_alunos):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    notas.append(nota)

media_turma = sum(notas) / qtd_alunos
print(f"As notas foram: {notas}")
print(f"A média da turma é: {media_turma:.2f}")
