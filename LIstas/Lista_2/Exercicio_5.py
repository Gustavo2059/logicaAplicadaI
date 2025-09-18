print('5 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:')
print(' - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;')
print(' - A mensagem "Reprovado", se a média for menor do que sete;')
print(' - A mensagem "Aprovado com Distinção", se a média for igual a dez;')

#declaracao

MEDIA = 7

#entradas

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2) / 2

if media >= MEDIA:
    if media == 10:
        print("Aprovado com distinção")
    else:
        print("Aprovado")
else:
    print("Reprovado")