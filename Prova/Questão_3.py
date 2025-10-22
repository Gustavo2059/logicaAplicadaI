tempos = []
for i in range(10):
    try:
        tempo = float(input(f'Digite a tempo do atleta {i+1}: '))
        tempos.append(tempo)
    except ValueError:
        print('Digite um valor válido')

if tempos:
    print(f'Melhor tempo: {min(tempos)}')
    print(f'Pior tempo: {max(tempos)}')
    print(f'Tempo médio: {sum(tempos)/len(tempos)}')


