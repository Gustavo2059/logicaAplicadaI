diasSemana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
entrada = input('Digite um valor equivalente a um dia da semana: ')
if not entrada.isnumeric():
    print('Valor inválido')
else:
    entrada = int(entrada)
    if 1 <= entrada <= 7:
        print(diasSemana[entrada - 1])
    else:
        print('Valor fora do intevalo')