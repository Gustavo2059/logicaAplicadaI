from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano:int):
        super().__init__(marca, modelo, ano)

    def mover(self):
        print('O carro está rodando nas quatro rodas')

palio = Carro('Fiat', 'Palio', 1999)
print(palio)
palio.mover()
