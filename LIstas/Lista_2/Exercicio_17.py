while True:
    ano = input('Digite um ano: ')
    if not ano.isnumeric():
        print('Digite um valor válido')
    else:
        ano = int(ano)
        break

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('É bisexto')
else:
    print('Não é bisexto')


