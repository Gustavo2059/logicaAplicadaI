from abc import ABC, abstractmethod
class Veiculo(ABC):
    def __init__(self, marca, modelo, ano:int):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def __str__(self):
        return (f'Marca: {self.marca}\n'
                f'Modelo: {self.modelo}\n'
                f'Ano: {self.ano}')

    @abstractmethod
    def mover(self):
        pass

