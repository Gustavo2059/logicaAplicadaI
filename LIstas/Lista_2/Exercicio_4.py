print('4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.')

#declaracao

vogais = ['a', 'e', 'i', 'o', 'u']

#entrada

entrada = input('Digite uma letra: ')

if entrada.isalpha() == True:
    if len(entrada) == 1:
        if entrada.lower() in vogais:
            print("A letra digitada é uma vogal")
        else:
            print("A letra digitada é consoante")
    else:
        print('Digite apenas uma letra')
else:
    print('Digito inválido')