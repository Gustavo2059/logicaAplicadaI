from animal import Animal

class Gato(Animal):
    def __init__(self, nome, idade, som):
        super().__init__(nome, idade, som)

    def som_animal(self):
        if self.som.lower() == 'miado':
            print(f'{self.nome} diz: miauuu')
        else:
            print('Valor inválido')

xaropinho = Gato('Xaropinho', 5, 'miado')
print(xaropinho)
xaropinho.som_animal()