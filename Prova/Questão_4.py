def analisar_vendas(vendas: list, venda5000: int):
    return (f'\nTotal de vendedores: {len(vendas)}'
            f'\nMaior venda: {max(vendas)}'
            f'\nMenor venda: {min(vendas)}'
            f'\nQuantidade de vendedores com vendas acima de R$5000: {venda5000}'
            f'\nMédia de vendas {sum(vendas)/len(vendas)}')

def main():
    vendas = []
    venda5000 = 0
    while True:
        try:
            venda = float(input('Insira o valor do venda (ou digite -1 para encerrar): '))
            if venda == -1:
                break
            vendas.append(venda)
            if venda > 5000:
                venda5000 = venda5000 + 1
        except ValueError:
            print('Erro')
    if vendas:
        print(analisar_vendas(vendas, venda5000))

if __name__ == '__main__':
    main()

