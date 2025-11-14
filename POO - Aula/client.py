#classes
class SavingsAccount():
    # constructor
    def __init__(self, number):
        #Privates atributes
        self.__number = number

    @property
    def number(self):
        return self.__number

    #setters
    @number.setter
    def number(self, number):
        self.__number = number

    def __str__(self):
        return f'Nome: {self.__number}'

#instances
savingsAccont = SavingsAccount(1234)


#exit
print(savingsAccont)