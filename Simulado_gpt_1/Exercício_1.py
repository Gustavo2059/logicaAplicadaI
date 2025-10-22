listIdade = []
maioridade = 0
for i in range(15):
    idade = int(input('Digite sua idade: '))
    listIdade.append(idade)
    if idade < 18:
        maioridade =+ 1
print(listIdade)
#saída
print(f'Maior idade: {max(listIdade)} ')
print(f'Menor idade: {min(listIdade)} ')
print(f'A média de idade é de: {sum(listIdade)/len(listIdade):.2f} ')
print(f'Quantidade de alunos com mais de 18 anos: {maioridade}')
