from abc import abstractmethod
#classe
class Animal():
    def __init__(self, nome, idade:int, som):
        self.nome = nome
        self.idade = idade
        self.som = som

    def __str__(self):
        return (f'Nome: {self.nome.title()}\n'
                f'Idade: {str(self.idade).title()}\n'
                f'Som característico: {self.som.title()}\n')

    @abstractmethod
    def som_animal(self):
        pass



