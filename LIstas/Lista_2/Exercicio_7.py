print('7 - Faça um Programa que leia três números e mostre o maior e o menor deles.')

#declaracoes
list = []

for i in range(3):
    numero = int(input('Digite um valor: '))
    list.append(numero)

#saida
print('Menor: ',min(list))
print('Maior: ',max(list))