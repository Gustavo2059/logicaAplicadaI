while True:
    x = input('Digite um lado do triangulo: ')
    if not x.isnumeric():
        print('Insira um valor numérico')
    else:
        x = float(x)
        break
while True:
    y = input('Digite outro lado do triangulo: ')
    if not y.isnumeric():
        print('Insira um valor numérico')
    else:
        y = float(y)
        break
while True:
    z = input('Digite outro lado do triangulo: ')
    if not z.isnumeric():
        print('Insira um valor numérico')
    else:
        z = float(z)
        break
if x + y > z and x + z > y and y + z > x:
    if x == y and x == z:
        print('O triângulo é equilátero')

    elif x == y and x != z or x == z and x != y or y == z and y != z:
        print('O triângulo é isósceles')
    else:
        print('O triângulo é escaleno')
else:
    print('Não é um triângulo')
