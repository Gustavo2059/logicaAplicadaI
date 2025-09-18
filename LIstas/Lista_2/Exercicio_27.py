fruta = input('Qual fruta vai comprar? ')
kg = int(input('Quantos quilogramas vai comprar? '))
if kg < 5:
    if fruta.lower() == 'morango':
        valor = kg * 2.5
    elif fruta.lower() == 'maca':
        valor = kg * 1.8
elif kg > 5:
    if fruta.lower() == 'morango':
        valor = kg * 2.2
    elif fruta.lower() == 'maca':
        valor = kg * 1.5

if valor > 25 or kg > 8:
   valor = valor * 0.9

print('Valor a ser pago: R$',valor)

