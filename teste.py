#Declarações
alunos = []
notas = []
media = []
situacao = []
#Classes
class Aluno:
    def __init__(self, nome, nota1, nota2, nota3):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.resultado = 0
        self.situacao = None

    def CalculoMedia(self):
        self.resultado = (sum([self.nota1, self.nota2, self.nota3]))/3
        return self.resultado

    def CalculoSituacao(self):
        if self.resultado < 3:
            self.situacao = "está reprovado"
        elif self.resultado <= 5:
            self.situacao = "está de recuperação"
        else:
            self.situacao = "está aprovado"
        return self.situacao


while True:
    inputAluno = input('Informe o nome do aluno (ou "sair" para encerrar): ')
    if inputAluno.lower() == 'sair':
        break
    else:
        alunos.append(inputAluno)
    inputNotas = float(input('Informe a nota do aluno: '))
    if inputNotas < 0 or inputNotas > 10:
        print('Nota inválida')
        break
    else:
        notas.append(inputNotas)

for x, y, z in zip(alunos, notas, ):



aluno = Aluno("joao", 1, 2, 3)

print(aluno.CalculoMedia())
print(aluno.nome)
