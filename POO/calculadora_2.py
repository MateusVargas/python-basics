class Calculadora:
    
    def __init__(self):
        pass # pass não faz nada,é só pra não deixar vazio

    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self,a, b):
        return a / b

calc = Calculadora() # instanciando
print(calc.somar(23,4))
print(calc.subtrair(2,78))
print(calc.multiplicar(8,9))
print(calc.dividir(12,7))