from televisor import Televisor
class SmartTv(Televisor):
    def __init__(self, marca, modelo, tamanho):
        super().__init__(marca, modelo, tamanho)
        self.numero_canais = 0
        self.volume = 0

    def ligar(self):
        print("Ligando Smart TV")

    def desligar(self):
        print("Desligando Smart TV")

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
        print('Conectando via Wi-Fi na Smart TV')


smart_tv = SmartTv('Samsung', 'Smart TV', 55)
smart_tv.ligar()
smart_tv.definir_numero_canais()
smart_tv.aumentar_canais()
smart_tv.diminuir_canais()
print(smart_tv.numero_canais)
smart_tv.aumentar_volume()
smart_tv.diminuir_volume()
print(smart_tv.volume)
smart_tv.conectar_internet()
smart_tv.desligar()
