#início
print("Lista 1 de exercícios de Lógica aplicada")
print("1° - Criar um algoritmo para ler os lados de um triângulo e identificar se é equilátero ")

#entradas

x = float(input("Digite o valor de um dos lados do triãngulo: "))
y = float(input("Digite outro valor de um lado: "))
z = float(input("Digite o último valor: "))

#condicionais

if x == y and x == z:
    print("O triângulo é equilátero")
else:
    print("O triângulo não é equilátero")

print("2° - Adapte o exemplo anterior para identificar um triângulo isósceles (2 lados iguais). ")

#entradas

x = float(input("Digite o valor de um dos lados do triãngulo: "))
y = float(input("Digite outro valor de um lado: "))
z = float(input("Digite o último valor: "))

#condicionais

if x == y and x != z or x == z and x != y or y == z and y != x:
    print("O triângulo é isósceles")
else:
    print("O triângulo não é isósceles")

print("3° - Adapte o algoritmo anterior para identificar o maior lado de um triângulo escaleno.")

list = []

#entradas

x = float(input("Digite o valor de um dos lados do triãngulo: "))
list.append(x)
y = float(input("Digite outro valor de um lado: "))
list.append(y)
z = float(input("Digite o último valor: "))
list.append(z)

#condicionais

if x != y and x != z and z != y:
    print("O triângulo é escaleno")
    print(f'Seu maior lado é: {max(list)}')
else:
    print("O triângulo não é escaleno")

print("4° - Faça um algoritmo que calcule a área de um Triângulo (os valores da base e altura devem ser lidos do teclado).")

#entradas

base = float(input("Digite o valor para a base do triãngulo: "))
altura = float(input("Digite o valor para a altura do triãngulo: "))

#Cálculo

area = (base * altura)/2

#Saída

print(f'A área do triângulo é: {area}')

print("5° - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 25% de desconto.")

#entrada

preco = float(input("Digite o preço do produto: "))

#cálculo

preco = preco - (preco * 0.25)

#saida

print(f'Preço com 25% de desconto é: {preco}')

print("6° - Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa em dias. Considerar ano com 365 dias e mês com 30 dias.")

#declaracoes

list = []

#entradas
list.append(int(input("Digite quantos anos você tem: ")))
list.append(int(input("E quantos meses? ")))
list.append(int(input("E quantos dias? ")))
#saida
print(f'{(list[0]*365) + (list[1]*30) + list[2]}')

print("7° - Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.")

#entradas
eleitores = int(input("Escreva a quantidade de eleitores no município: "))
brancos = int(input("Escreva a quantidade de votos em branco do município: "))
nulos = int(input("Escreva a quantidade de votos nulos do município: "))
validos = int(input("Escreva a quantidade de votos válidos do município: "))

total = brancos+nulos+validos
if total != eleitores:
    print("Os dados inseridos estão incompletos")
else:
    print("Dados inseridos com sucesso")
    print(f'Percentual de votos válidos: {(total*validos)/100}%')
    print(f'Percentual de votos em branco: {(total*brancos)/100}%')
    print(f'Percentual de votos nulos: {(total*nulos)/100}%')
