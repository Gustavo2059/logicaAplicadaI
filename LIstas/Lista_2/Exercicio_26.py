combustivel = input('Qual combustível vai utilizar? (G) - Gasolina (A) - Álcool: ')
combustivel = combustivel.upper()
quantidade = float(input('Quantos litros de combustível? '))

if combustivel == 'G':
    valorB = quantidade * 2.5
    if quantidade < 20:
        valorF = valorB * 0.96
    else:
        valorF = valorB * 0.94
else:
    valorB = quantidade * 1.9
    if quantidade < 20:
        valorF = valorB * 0.97
    else:
        valorF = valorB * 0.95


print(valorF)