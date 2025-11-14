#classes
class Account():
    # constructor
    def __init__(self, agency, code):
        #Privates atributes
        self.__agency = agency
        self.__code = code

    @property
    def agency(self):
        return self.__agency
    @property
    def code(self):
        return self.__code

    #setters
    @agency.setter
    def agency(self, agency):
        self.__agency = agency

    @code.setter
    def code(self, code):
        self.__code = code

    def __str__(self):
        return (
            f'Agência: {self.__agency}\n'
            f'Código: {self.__code}\n')

#instances
account = Account(146549,
                1234)
#exit
print(account)