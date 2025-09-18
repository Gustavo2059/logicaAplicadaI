valor = int(input('Digite um valor: '))
if 10 <= valor <= 600:
    nota100 = valor // 100
    valor %= 100
    nota50 = valor // 50
    valor %= 50
    nota10 = valor // 10
    valor %= 10
    nota5 = valor // 5
    valor %= 5
    nota1 = valor // 1
    valor %= 1
    print('Notas entregues')
    if nota100 > 0:
        print(f'Nota 100: {nota100}')
    if nota50 > 0:
        print(f'Nota 50: {nota50}')
    if nota10 > 0:
        print(f'Nota 10: {nota10}')
    if nota5 > 0:
        print(f'Nota 5: {nota5}')
    if nota1 > 0:
        print(f'Nota 1: {nota1}')
else:
    print('Valor inválido')