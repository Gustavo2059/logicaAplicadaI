print('3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.')

#entrada

letra = input('Digite F ou M: ')
if letra.upper() == 'F':
    print('F - Feminino')
elif letra.upper() == 'M':
    print('M - Masculino')
else:
    print('Digito inválido')