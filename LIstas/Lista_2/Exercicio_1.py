print('1 - Faça um Programa que peça dois números e imprima o maior deles.')
list = []
#entrada
primeiroNumero = int(input('Digite o primeiro número: '))
list.append(primeiroNumero)
segundoNumero = int(input('Digite o segundo: '))
list.append(segundoNumero)

#saida
print(max(list))