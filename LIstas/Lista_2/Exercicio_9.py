print('9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.')
list = []
for i in range(3):
    numero = int(input('Digite um valor: '))
    list.append(numero)
print(sorted(list, reverse=True))