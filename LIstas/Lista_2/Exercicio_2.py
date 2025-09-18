print('2 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.')

#entradas
valor = int(input('Digite um valor: '))

#condicoes

if valor > 0:
    print('O valor é positivo')
elif valor < 0:
    print('O valor é negativo')
else:
    print('Zero é neutro')