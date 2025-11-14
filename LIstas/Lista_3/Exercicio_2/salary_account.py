#Importações
from account import Account

#Classes
class SalaryAccount(Account):
    #Representação de uma conta corrente
    #Constructor herdando atributos da classe Account
    def __init__(self, account_number, account_dig, balance, agency, agency_dig, code):
        super().__init__(agency, agency_dig, code)
        self.__account_number = account_number
        self.__account_dig = account_dig
        self.__balance = balance

    #Getters
    @property
    def account_number(self):
        return self.__account_number
    @property
    def account_dig(self):
        return self.__account_dig
    @property
    def balance(self):
        return self.__balance

    #Setters

    @account_number.setter
    def account_number(self, account_number):
        self.__account_number = account_number

    @account_dig.setter
    def account_dig(self, account_dig):
        self.__account_dig = account_dig

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    def __str__(self):
        return (
            f"Número da conta: {self.__account_number}-{self.__account_dig}\n"
            f"Saldo: {self.__balance}"
        )

    def add_money(self, add_balance):
        if add_balance > 0:
            self.__balance += add_balance
            print('Saldo Atualizado!')
        else:
            print('Você não pode adicionar valores negativos ao saldo!')


    def with_draw_money(self, draw_money):
        #sacar dinheiro
        self.__balance -= draw_money
        print('Saque realizado com sucesso!')
