import tabulate
def analisar_salario(lista: list):
    salario3000 = 0
    for salario in lista:
        if salario > 3000:
            salario3000 =+ 1
    return (f'Número de funcionários: {len(lista)} '
            f'\nO maior salário é: {max(lista)} '
            f'\nO menor salário é {min(lista)} '
            f'\nFuncionários que ganham acima de R$3000,00: {salario3000} '
            f'\nMédia dos salários: {sum(lista)/len(lista)}')
def main():
    lista = []


    while True:
        salario = input('Digite o salário (ou -1 para sair): ')
        if salario == '-1':
            print('\nPrograma finalizado')
            break
        elif salario.isnumeric():
            salario = int(salario)
            lista.append(salario)
        else:
            print('\nDigite um valor válido')
            continue
    if len(lista) > 0:
        print(analisar_salario(lista))

if __name__ == '__main__':
    main()

