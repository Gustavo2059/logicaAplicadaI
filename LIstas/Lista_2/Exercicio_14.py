while True:
    nota1 = input('Digite sua primeira nota: ')
    if not nota1.isnumeric():
        print('Valor inválido')
    else:
        nota1 = float(nota1)
        break
while True:
    nota2 = input('Digite sua segunda nota: ')
    if not nota2.isnumeric():
        print('Valor inválido')
    else:
        nota2 = float(nota2)
        break

#calculo de media
media = (nota1 + nota2) / 2

if media <= 4:
    conceito = 'E'
elif media <= 6:
    conceito = 'D'
elif media <= 7.5:
    conceito = 'C'
elif media <= 9:
    conceito = 'B'
elif media <= 10:
    conceito = 'A'

#saida
print('Primeira nota: ', nota1)
print('Segunda nota: ', nota2)
print('Média: ', media)
print('Conceito: ', conceito)
if conceito == 'D' or conceito == 'E':
    print('Reprovado')
else:
    print('Aprovado')
