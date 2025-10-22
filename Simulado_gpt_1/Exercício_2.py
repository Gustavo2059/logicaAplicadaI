def analisar_temperaturas(temperaturas: list):
    return (f'\nA temperatura máxima é de: {max(temperaturas)}'
            f'\nA temperatura mínima é de: {min(temperaturas)}'
            f'\nA média das temperaturas é de {sum(temperaturas)/len(temperaturas)}')



def main():
    temperaturas = []
    for i in range(5):
        try:
            temperatura = float(input('Digite a temperatura: '))
            temperaturas.append(temperatura)
        except ValueError:
            print('Erro')

    print(analisar_temperaturas(temperaturas))

if __name__ == '__main__':
    main()

