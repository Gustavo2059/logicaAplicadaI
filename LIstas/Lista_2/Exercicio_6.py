print('6 - Faça um Programa que leia três números e mostre o maior deles.')

#declaracoes
list = []

for i in range(3):
    numero = int(input('Digite um valor: '))
    list.append(numero)

#saida
print(max(list))