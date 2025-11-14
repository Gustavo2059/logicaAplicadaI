class Veiculo():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def __str__(self):
        return (f'Marca: {self.marca}\n'
                f'Modelo: {self.modelo}\n'
                f'Ano: {self.ano}')

    def mover(self):
        return f'O Veículo está rodando em {None}'

