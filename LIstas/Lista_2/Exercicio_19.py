while True:
    n = input('Digite um número menor que 1000: ')
    if not n.isnumeric():
        print('Valor inválido')
    elif int(n) > 1000:
        print('Valor inválido')
    else:
        break

list = list(n)
listS = []

if len(list) == 3:
    for i in list:
        if i == '1':
            listS.append('')
        else:
            listS.append('s')
    print(f'{n} = {list[0]} centena{listS[0]}, {list[1]} dezena{listS[1]} e {list[2]} unidade{listS[2]}')
elif len(list) == 2:
    for i in list:
        if i == '1':
            listS.append('')
        else:
            listS.append('s')
    print(f'{n} = {list[0]} dezena{listS[0]} e {list[1]} unidade{listS[1]}')
else:
    for i in list:
        if i == '1':
            listS.append('')
        else:
            listS.append('s')
    print(f'{n} = {list[0]} unidade{listS[0]}')


