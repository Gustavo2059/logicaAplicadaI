list = []
MEDIA = 6
acimaMedia = 0
for i in range(15):
    while True:
        nota = input('Digite a nota: ')
        if nota.isnumeric():
            nota = float(nota)
            if 0 < nota < 10:
                list.append(nota)
                break
            else:
                print('Digite um valor no intervalo entre 0 e 10')
                continue
        else:
            print('Digite em valor válido')
            continue

for notas in list:
    if notas > MEDIA:
        acimaMedia += 1

print(f'Maior nota: {max(list)}')
print(f'Menor nota: {min(list)}')
print(f'Média da turma: {sum(list)/len(list)}')
print(f'Quantidade de alunos acima da média: {acimaMedia}')