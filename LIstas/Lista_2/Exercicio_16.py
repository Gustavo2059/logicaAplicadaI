a = int(input('Digite um valor para A: '))
if a != 0:
    b = int(input('Digite um valor para B: '))
    c = int(input('Digite um valor para C: '))
    #calculo do delta
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print('A equação não possui raízes reais')
    else:
    #Bhaskara
    x1 = (-b + (delta**(1/2))) / (2 * a)
    x2 = (-b - (delta**(1/2))) / (2 * a)
    if delta == 0:
        print('A equação possui uma apenas raíz real: ', x1)
    else:
        print('A equação possui duas raízes reais: ', x1, x2)
else:
    print('O valor de A não pode ser 0')


