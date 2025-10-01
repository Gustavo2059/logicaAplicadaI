def classificar_imc (nome: str, imc: float) -> str:
    if imc < 18.5:
        return f'{nome} está abaixo do peso'
    elif imc < 24.9:
        return f'{nome} está com o peso normal'
    elif imc < 29.9:
        return f'{nome} está com sobre peso'
    else:
        return f'{nome} está obeso'

listNomes = []
listImc = []

while True:
    nome = input('Digite um nome ou ("sair" para encerrar): ')
    if not nome.isalpha():
        print('Digite um nome válido')
        continue
    elif nome.lower() == 'sair':
        break
    else:
        listNomes.append(nome)
        while True:
            imc = input('Digite o imc: ')
            if not imc.isnumeric():
                print('Digite um valor válido')
                continue
            else:
                imc = float(imc)
                listImc.append(imc)
                break

for i, x in zip(listNomes, listImc):
    print(classificar_imc(i, x))







