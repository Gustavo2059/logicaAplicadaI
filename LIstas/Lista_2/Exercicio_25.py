verificador = 0
x = input('Telefonou para a vítima? (S) ou (N): ')
if x.lower() == 's':
    verificador += 1
x = input('Esteve no local do crime? (S) ou (N): ')
if x.lower() == 's':
    verificador += 1
x = input('Mora perto da vítima? (S) ou (N): ')
if x.lower() == 's':
    verificador += 1
x = input('Devia para a vítima? (S) ou (N): ')
if x.lower() == 's':
    verificador += 1
x = input('Já trabalhou com a vítima? (S) ou (N): ')
if x.lower() == 's':
    verificador += 1

if verificador == 2:
    print('Suspeito')
elif verificador == 3 or verificador == 4:
    print('Cúmplice')
elif verificador == 5:
    print('Assassino')
else:
    print('Inocente')