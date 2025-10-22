def avaliar_idade(nome: str, idade: int):
    if idade < 12:
        return f'{nome} é uma criança'
    elif idade <= 17:
        return f'{nome} é um adolescente'
    elif idade <= 59:
        return f'{nome} é um adulto'
    else:
        return f'{nome} é um idoso'

def main():
    pessoas = []
    idades = []
    while True:
        nome = input('Digite seu nome (ou digite "fim" para encerrar): ')
        if nome == 'fim':
            print('Encerrando o programa')
            break
        try:
            idade = int(input('Digite sua idade: '))
            print(f'Nome: {nome}')
            print(f'Idade: {idade}')
            print(f'Resultado: {avaliar_idade(nome, idade)}')
        except ValueError:
            print('Erro')

if __name__ == '__main__':
    main()



