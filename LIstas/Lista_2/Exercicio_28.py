carne = input('Qual carne vai comprar? ')
kg = int(input('Quantos quilogramas vai comprar? '))
cartao = input('Possui cartão Tabajara? ')
if kg < 5:
    if carne.lower() == 'file duplo':
        valor = kg * 4.9
    elif carne.lower() == 'alcatra':
        valor = kg * 5.9
    elif carne.lower() == 'picanha':
        valor = kg * 6.9
elif kg > 5:
    if carne.lower() == 'file duplo':
        valor = kg * 5.8
    elif carne.lower() == 'alcatra':
        valor = kg * 6.8
    elif carne.lower() == 'picanha':
        valor = kg * 7.8

if cartao.lower() == 's':
    desconto = valor * 0.05
    pagamento = 'Cartão Tabajara'
else:
    desconto = 0
    pagamento = 'Normal'

print('Nota fiscal: ')
print('Tipo de carne: ', carne)
print('Quilos comprados: ', kg)
print('Preço total: ', valor)
print('Tipo de pagamento: ', pagamento)
print('Desconto: ', desconto)
print('Valor a ser pago: R$',valor - desconto)