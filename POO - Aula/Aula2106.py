#classes
class Client():
    # constructor
    def __init__(self, name, cpf, address, addressNumber, addressComplement, dtBirth, phone, email):
        #Privates atributes
        self.__name = name
        self.__cpf = cpf
        self.__address = address
        self.__addressNumber = addressNumber
        self.__addressComplement = addressComplement
        self.__dtBirth = dtBirth
        self.__phone = phone
        self.__email = email

    @property
    def name(self):
        return self.__name
    @property
    def cpf(self):
        return self.__cpf
    @property
    def address(self):
        return self.__address
    @property
    def addressNumber(self):
        return self.__addressNumber
    @property
    def addressComplement(self):
        return self.__addressComplement
    @property
    def dtBirth(self):
        return self.__dtBirth
    @property
    def phone(self):
        return self.__phone
    @property
    def email(self):
        return self.__email

    #setters
    @name.setter
    def name(self, name):
        self.__name = name

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @address.setter
    def address (self, addressNumber):
        self.__addressNumber = addressNumber

    @addressNumber.setter
    def addressNumber(self, addressNumber):
        self.__addressNumber = addressNumber

    @addressComplement.setter
    def addressComplement(self, addressComplement):
        self.__addressComplement = addressComplement

    @dtBirth.setter
    def dtBirth(self, dtBirth):
        self.__dtBirth = dtBirth

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @email.setter
    def email(self, email):
        self.__email = email

    def __str__(self):
        return (
            f'Nome: {self.__name}\n'
            f'CPF: {self.__cpf}\n'
            f'Endereço: {self.__address} {self.__addressNumber} {self.__addressComplement}\n'
            f'Data de nascimento: {self.__dtBirth}\n'
            f'Telefone: {self.__phone}\n'
            f'Email: {self.__email}\n'
        )

#instances
client = Client("Gustavo Mai",
                10553823990,
                "Rua Maria Eduarda",
                205,
                "Portão azul",
                "29/03/2007",
                48991779664,
                "gustavomai2059@gmail.com")


#exit
print(client)