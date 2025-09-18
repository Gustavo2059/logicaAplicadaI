hora = input('Digite a quantidade de horas trabalhadas: ')
hora = float(hora)
valorHora = input('Digite o valor da hora trabalhada: ')
valorHora = float(valorHora)
salarioB = hora * valorHora

#imposto de renda
if salarioB <= 900:
    IR = "Isento"
    descontoIR = 0
elif salarioB <= 1500:
    IR = 5
    descontoIR =  salarioB * 0.05
elif salarioB <= 2500:
    IR = 10
    descontoIR = salarioB * 0.1
else:
    IR = 20
    descontoIR = salarioB * 0.2


#fgts(não descontado)
descontofgts = salarioB * 0.11
#INSS
descontoINSS = salarioB * 0.10
#calculo
salarioLiquido = (salarioB - descontoIR - descontoINSS)
totalDescontos = (descontoIR + descontoINSS)
#saida
print('Salário Bruto: R$', salarioB)
print('(-) IR (',IR,'%) : R$', descontoIR)
print('(-) INSS (10%) : R$', descontoINSS)
print('FGTS (11%): R$', descontofgts)
print('Total de descontos: R$', totalDescontos)
print('Salário líquido: R$', salarioLiquido)
