class Account():
    #Clase que representa uma conta bancária
    #constructor
    def __init__(self, agency:int, agency_dig:int, code:int):
        self.__agency = agency
        self.__agency_dig = agency_dig
        self.__code = code

        #Getters

    @property
    def agency(self):
        return self.__agency
    @property
    def agency_dig(self):
        return self.__agency_dig
    @property
    def code(self):
        return self.__code

        #Setters

    @agency.setter
    def agency(self, agency):
        self.__agency = agency

    @agency_dig.setter
    def agency_dig(self, agency_dig):
        self.__agency_dig = agency_dig

    @code.setter
    def code(self, code):
        self.__code = code

    def __str__(self):
        return (f'Agência: {self.__agency}-{self.__agency_dig}\n'
                f'Código do banco: {self.__code}')

    def update_balance(self):
        resposta = input('Digite o novo valor de saldo\n')
        self.__balance = float(resposta)
        print("Valor atualizado!")



