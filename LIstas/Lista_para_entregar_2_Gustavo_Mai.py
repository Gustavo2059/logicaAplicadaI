'''print('1 - Faça um Programa que peça dois números e imprima o maior deles.')

#entrada
primeiroNumero = int(input('Digite o primeiro número: '))
segundoNumero = int(input('Digite o segundo: '))

#saida
print(f'O primeiro número é: {primeiroNumero} e o segundo é: {segundoNumero}')'''


'''print('2 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.')

#entradas
valor = int(input('Digite um valor: '))

#condicoes

if valor > 0:
    print('O valor é positivo')
elif valor < 0:
    print('O valor é negativo')
else:
    print('Zero é neutro')'''

'''print('3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.')

#entrada

letra = input('Digite F ou M: ')
if letra.upper() == 'F':
    print('F - Feminino')
elif letra.upper() == 'M':
    print('M - Masculino')
else:
    print('Digito inválido')'''

'''print('4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.')

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
    print('Digito inválido')'''

'''print('5 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:')
print(' - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;')
print(' - A mensagem "Reprovado", se a média for menor do que sete;')
print(' - A mensagem "Aprovado com Distinção", se a média for igual a dez;')

#declaracao

MEDIA = 7

#entradas

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2) / 2

if media >= MEDIA:
    if media == 10:
        print("Aprovado com distinção")
    else:
        print("Aprovado")
else:
    print("Reprovado")'''

'''print('6 - Faça um Programa que leia três números e mostre o maior deles.')

#declaracoes
list = []

for i in range(3):
    numero = int(input('Digite um valor: '))
    list.append(numero)

#saida
print(max(list))'''

'''print('7 - Faça um Programa que leia três números e mostre o maior e o menor deles.')

#declaracoes
list = []

for i in range(3):
    numero = int(input('Digite um valor: '))
    list.append(numero)

#saida
print(min(list))'''

print('8 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.')

#declaracoes
listProduto = []
listValor = []

for i in range(3):
    produto = input('Digite o produto: ').lower()
    while True:
        if produto.isalpha() == True:
            listProduto.append(produto)
            break
        else:
            print('Produto inválido')

    preco = input('Digite um valor: ')

    while True:
        if preco.isnumeric() == True:
            preco = float(preco)
            listValor.append(preco)
            break
        else:
            print('Preço inválido')


print(listProduto)
print(listValor)




