def contar_pares_impares(lista: list):
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)


def main():
    lista = []
    pares = []
    impares = []

    for i in range(3):
        try:
            numero = int(input('Insira o número: '))
            lista.append(numero)
        except ValueError:
            print('Erro')

    print(contar_pares_impares(lista))

if __name__ == '__main__':
    main()
