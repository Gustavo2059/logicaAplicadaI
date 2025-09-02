#Testes de variáveis

#import
import array as arr


#Declarações
firstName = "João"
lastName = "Silva"
name = firstName + " " + lastName
valorHora = 45.36  #Tipagem dinâmica
valorHoraAprox = int(valorHora)
diasTrabalhados = 30
HORASTRABALHADAS = 8
HORASTRABALHADASAJUST = float(HORASTRABALHADAS)
vencimento = (HORASTRABALHADASAJUST * valorHora) * diasTrabalhados

dadosFuncionarios = [firstName, lastName, vencimento]
dadosFuncionarios = dadosFuncionarios.append(diasTrabalhados)

valores = arr.array('f', [valorHora, HORASTRABALHADAS])

#Saídas
print("Funcionário")
print(firstName, lastName)
print("Salário/mês")
print(valores)