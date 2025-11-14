from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano:int):
        super().__init__(marca, modelo, ano)

    def mover(self):
        print('A moto está rodando em duas rodas')

titan = Moto('Honda', 'Cg Titan', 2001)
print(titan)
titan.mover()
