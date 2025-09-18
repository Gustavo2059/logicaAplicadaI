n1 = input('Digite um valor: ')
n2 = input('Digite outro valor: ')
print('Qual operação você deseja realizar?')
print('(1) - Soma')
print('(2) - Subtração')
print('(3) - Multiplicacao')
print('(4) - Divisão')
print('-----------------------------------')
op = input()
n1 = float(n1)
n2 = float(n2)
if op == '1':
    resultado = (n1 + n2)
elif op == '2':
    resultado = (n1 - n2)
elif op == '3':
    resultado = (n1 * n2)
else:
    resultado = (n1/n2)

if resultado > 0:
    sinal = 'positivo'
elif resultado == 0:
    sinal = 'Nêutro'
else:
    sinal = 'negativo'

if resultado.is_integer():
    inteiro_ou_decimal = 'inteiro'
    if resultado % 2 == 0:
        par_ou_impar = 'Par'
    else:
        par_ou_impar = 'Impar'
else:
    inteiro_ou_decimal = 'decimal'
    par_ou_impar = ('Par ou ímpar só se aplica a números inteiros')

print('Resultado: ', resultado)
print('-----------------------')
print('Par ou ímpar?', par_ou_impar)
print('O sinal é', sinal)
print('O número é', inteiro_ou_decimal)