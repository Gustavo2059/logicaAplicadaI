from animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, idade, som):
        super().__init__(nome, idade, som)

    def som_animal(self):
        if self.som.lower() == 'latido':
            print(f'{self.nome} diz: auau')
        else:
            print('Valor inválido')


ted = Cachorro('Ted', 5, 'latido')
print(ted)
ted.som_animal()