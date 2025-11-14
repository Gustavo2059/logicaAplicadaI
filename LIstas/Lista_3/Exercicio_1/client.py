class Client():
#Classe que representa um cliente e seus dados
    #constructor
    def __init__(self,name, cpf:int, address, addressNumber:int, addressComplement, dtBirth, phone:int, email):
        #atributos privados
        self.__name = name
        self.__cpf = cpf
        self.__address = address
        self.__addressNumber = addressNumber
        self.__addressComplement = addressComplement
        self.__dtBirth = dtBirth
        self.__phone = phone
        self.__email = email

    #Getters - Forma controlada de acessar atributos privados

    @property  # faz com que um metodo se comporte como atributo
    def name(self):
        return self.__name

    @property
    def cpf(self):
        return self.__cpf

    @property
    def address(self):
        return self.__address

    @property
    def address_number(self):
        return self.__addressNumber

    @property
    def address_complement(self):
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

    #Setters - Permite que os atributos sejam modificados

    @name.setter
    def name(self, name):
        self.__name = name

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @address.setter
    def address(self, address):
        self.__address = address

    @address_number.setter
    def address_number(self, address_number):
        self.__address_number = address_number

    @address_complement.setter
    def address_complement(self, address_complement):
        self.__address_complement = address_complement

    @dtBirth.setter
    def dt_birth(self, dtBirth):
        self.__dtBirth = dtBirth

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @email.setter
    def email(self, email):
        self.__email = email

    #Funções

    def __str__(self): #fornece uma string com os atributos da classe
        return (f'Nome: {self.__name}'
                f'\nCPF: {self.__cpf}'
                f'\nAddress: {self.__address}'
                f'\nAddress Number: {self.__addressNumber}'
                f'\nAddress Complement: {self.__addressComplement}'
                f'\nData de nascimento: {self.__dtBirth}'
                f'\nPhone: {self.__phone}'
                f'\nEmail: {self.__email}')

    def update_person(self):
        #permite que os atributos sejam atualizados
        while True:
            print('Que informação deseja atualizar?\n'
                  '(1) - Nome\n'
                  '(2) - CPF\n'
                  '(3) - Endereço\n'
                  '(4) - Número do endereço\n'
                  '(5) - Complemento\n'
                  '(6) - Data de nascimento\n'
                  '(7) - Telefone\n'
                  '(8) - Email\n')

            resposta = input(">>>")

            if resposta == '1':
                self.__name = input('Nome: ')
                print('Valor atualizado!')
                break

            elif resposta == '2':
                self.__cpf = input('CPF: ')
                print('Valor atualizado!')
                break
            elif resposta == '3':
                self.__address = input('Endereço: ')
                print('Valor atualizado!')
                break
            elif resposta == '4':
                self.__addressNumber = input('Número do endereço: ')
                print('Valor atualizado!')
                break
            elif resposta == '5':
                self.__addressComplement = input('Complemento: ')
                print('Valor atualizado!')
                break
            elif resposta == '6':
                self.__dtBirth = input('Data de nascimento: ')
                print('Valor atualizado!')
                break
            elif resposta == '7':
                self._phone = input('Telefone: ')
                print('Valor atualizado!')
                break
            elif resposta == '8':
                self.__email = input('email: ')
                print('Valor atualizado!')
                break