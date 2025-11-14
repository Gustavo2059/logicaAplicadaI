from abc import abstractmethod
from conectividade import Conectividade

class Televisor(Conectividade):
    def __init__(self, marca, modelo, tamanho:int):
        self.marca = marca
        self.modelo = modelo
        self.tamanho = tamanho

    def __str__(self):
        print(str(f'Marca: {self.marca}\n'
              f'Modelo: {self.modelo}\n'
              f'Tamanho: {self.tamanho}\n'))

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @abstractmethod
    def definir_numero_canais(self ):
        pass

    @abstractmethod
    def aumentar_canais(self):
        pass

    @abstractmethod
    def diminuir_canais(self):
        pass

    @abstractmethod
    def aumentar_volume(self):
        pass

    @abstractmethod
    def diminuir_volume(self):
        pass
