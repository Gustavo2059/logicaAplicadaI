from televisor import Televisor

class TvComum(Televisor):
    def __init__(self, marca, modelo, tamanho:int):
        super().__init__(marca, modelo, tamanho)
        self.numero_canais = 0
        self.volume = 0

    def ligar(self):
        print("Ligando tv comum")

    def desligar(self):
        print("Desligando tv comum")

    def definir_numero_canais(self):
        resposta = int(input('Insira o numero de canais: '))
        self.numero_canais = resposta

    def aumentar_canais(self):
        resposta = int(input('Insira o numero de canais a serem adicionados: '))
        if resposta > 0:
            self.numero_canais += resposta
        else:
            print('Valor inválido')

    def diminuir_canais(self):
        resposta = int(input('Insira o numero de canais a serem retirados: '))
        if resposta > 0:
            self.numero_canais -= resposta
        else:
            print('Valor inválido')

    def aumentar_volume(self):
        resposta = int(input('Digite o acréscimo de volume desejado: '))
        if resposta > 0:
            self.volume += resposta
        else:
            print('Valor inválido')

    def diminuir_volume(self):
        resposta = int(input('Digite o decréscimo de volume desejado: '))
        if resposta > 0:
            self.volume -= resposta
        else:
            print('Valor inválido')

    def conectar_internet(self):
        print('Não é possível conectar essa tv à internet')

tv = TvComum('Toschiba', 'veia', 14)
tv.ligar()
tv.definir_numero_canais()
tv.aumentar_canais()
tv.diminuir_canais()
print(tv.numero_canais)
tv.aumentar_volume()
tv.diminuir_volume()
print(tv.volume)
tv.conectar_internet()
tv.desligar()