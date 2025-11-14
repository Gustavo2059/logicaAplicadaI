#classe
class Animal():
    def __init__(self, nome, idade, som):
        self.nome = nome
        self.idade = str(idade)
        self.som = som

    def __str__(self):
        return (f'Nome: {self.nome.title()}\n'
                f'Idade: {self.idade.title()}\n'
                f'Som característico: {self.som.title()}\n')



