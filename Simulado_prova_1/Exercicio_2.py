def classificar_imc (nome: str, imc: float) -> str:
    if imc < 18.5:
        return f'{nome} está abaixo do peso'
    elif imc < 24.9:
        return f'{nome} está com o peso normal'
    elif imc < 29.9:
        return f'{nome} está com sobre peso'
    else:
        return f'{nome} está obeso'

def main():
    list = [] #armazena nome, imc e classificação

    while True:
        nome = input('Digite um nome ou ("sair" para encerrar): ')
        if nome.lower() == 'sair':
            print('\n Programa encerrado')
            break
        try:
            imc = float(input('Digite o IMC: '))
            classificacao = classificar_imc(nome, imc)
            list.append((nome, imc, classificacao))
        except ValueError:
            print("Erro: Digite um valor válido")

    if list:
        print('\n Ranking de IMC (crescente)')
        list_ordenada = sorted(list, key=lambda item: item[1])
        for pos, (nome, imc, classificacao) in enumerate(list_ordenada, start=1):
            print(f'{pos}° lugar - {nome}: IMC = {imc:.2f} -> {classificacao}')

        imcs = [imc for _, imc, _ in list]
        media_imc = sum(imcs)/len(imcs)
        print(f'\nMédia dos IMCs: {media_imc:.2f}')

if __name__ == '__main__':
    main()










