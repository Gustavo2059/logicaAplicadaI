from abc import ABC, abstractmethod
class Conectividade(ABC):

    @abstractmethod
    def conectar_internet(self):
        pass