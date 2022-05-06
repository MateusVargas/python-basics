from televisao import Televisao
from calculadora import Calculadora
from contar_letras import conta_letras,teste

if __name__ == "__main__":
    tv = Televisao()
    print(tv.ligada)
    tv.power()
    print(tv.ligada)

    calc = Calculadora(3,9)
    print(calc.somar())

    lista = ['palavra', 'jogo']
    print(conta_letras(lista))
    print(teste())