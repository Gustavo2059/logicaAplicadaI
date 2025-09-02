#Aula Revisão


#Declarações
MEDIA = 6
MIN = 3
listAluno = []
listNota = []
listSituacao = []
while True:
    aluno = input("Digite o nome do aluno, ou -1 para sair:  ")
    validacao = aluno.isalpha()
    if validacao == False:
        print("Digite um nome válido")
        break
    elif aluno == "-1":
        break

    listAluno.append(aluno)
    nota = float(input("Digite a nota do aluno: "))
    listNota.append(nota)
    if nota <= MEDIA and nota >= MIN:
        listSituacao.append("está em recuperação")
    elif nota < MEDIA:
        listSituacao.append("está reprovado")
    else:
        listSituacao.append("está aprovado")

for x, y, z in zip(listAluno, listNota, listSituacao):
    print(f'O aluno {x} teve média {y} e está {z}')





