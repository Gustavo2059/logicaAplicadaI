print('As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.')
print('Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:')
print('salários até R$ 280,00 (incluindo) : aumento de 20%')
print('salários entre R$ 280,00 e R$ 700,00 : aumento de 15%')
print('salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%')
print('salários de R$ 1500,00 em diante : aumento de 5%')
print('Após o aumento ser realizado, informe na tela:')
print('o salário antes do reajuste;')
print('o percentual de aumento aplicado;')
print('o valor do aumento;')
print('o novo salário, após o aumento')

salario = input('Digite o valor do seu salario: ')
salario = float(salario)

if salario <= 280:
    aumento = salario * 0.20
    percentual = 20
elif salario <= 700:
    aumento = salario * 0.15
    percentual = 15
elif salario <= 1500:
    aumento = salario * 0.10
    percentual = 10
else:
    aumento = salario * 0.05
    percentual = 5

print(f'O salário inicial: R${salario}')
print(f'Aumento: {aumento} ({percentual}%).')
print(f'Total do reajuste: R$ {salario + aumento}.')
