notas = []

while True:
    nome = input('Informe o nome do aluno: ')
    try:
        nota = float(input('Digite um nota (digite um número negativo para encerrar): '))
        if nota < 0:
            break
        notas.append(nota)
    except ValueError:
        print('Erro')
        continue

#saidas
if notas:
    print(f'Quantidade de alunos: {len(notas)}')
    print(f'Maior nota: {max(notas)}')
    print(f'Menor nota: {min(notas)}')
    print(f'Média da turma: {sum(notas) / len(notas)}')