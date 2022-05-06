class Error(Exception):#criando classe que herda de Exception
    pass

class InputError(Error):#criando classe de exceção, parenteses significam herança
    def __init__(self, message):
        self.message = message

while True:
    try:
        a = float(input('Entre com uma nota de 0 a 10: '))
        print(a)
        if a > 10:
            raise InputError('nota não pode ser maior que 10')# raise lança uma exceção
        elif a < 0:
            raise InputError('nota não pode ser negativa')
        break
    except ValueError:
        print('digite apenas números')
    except InputError as ex:
        print(ex)
