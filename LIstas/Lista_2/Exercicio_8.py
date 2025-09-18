print('8 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.')

#declaracoes
listProduto = []
listValor = []
for i in range(3):
    produto = input('Digite o produto: ').lower()
    avisou = False
    while not produto.isalpha():
        if not avisou:
            print('Produto inválido')
            avisou = True
        produto = input('Digite o produto: ').lower()
    listProduto.append(produto)

    preco = input('Digite um valor: ')
    avisou = False
    while not preco.isnumeric():
        if not avisou:
            print('Preço inválido')
            avisou = True
        preco = input('Digite um valor: ').lower()
    preco = float(preco)
    listValor.append(preco)

minimo = min(listValor)
for x, y in zip(listValor, listProduto):
    if x == minimo:
        produtoMinino = y

print(f'O produto de menor valor é {produtoMinino}')