listN = []
for i in range(3):
    n = int(input('Digine a nota: '))
    listN.append(n)

media = sum(listN) / len(listN)

if media == 10:
    print('Aprovado com distinção')
elif media >= 7:
    print('Aprovado')
elif media < 7:
    print('Reprovado')




