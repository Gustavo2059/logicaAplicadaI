bisexto = False
while True:
    data = input('Digite a data no formato dd/mm/aaaa: ')
    if not len(data) == 10:
        print('Data inválida (use as barras)')
    else:
        dia = int(data[0:2])
        mes = int(data[3:5])
        ano = int(data[6:10])
        break

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    bisexto = True

mesesVerifica = [1, 3, 5, 7, 8, 10, 12]
if ano >= 0 and 1 <= mes <= 12:
    if mes in mesesVerifica:
        if 1 <= dia <= 31:
            print('Data válida')
        else:
            print('Data inválida')
    elif mes == 2:
        if bisexto == True:
            if 1 <= dia <= 29:
                print('Data válida')
            else:
                print('Data inválida')
        elif 1 <= dia <= 28:
            print('Data válida')
        else:
            print('Data inválida')
    else:
        if 1 <= dia <= 30:
            print('Data válida')
        else:
            print('Data inválida')
else:
    print('Data inválida')