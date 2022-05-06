a = int(input('digite o valor de A: '))
b = int(input('digite o valor de B: '))

# && => and
# || => or
# ! => not

def verifica():
    if a > b and a > -1 and b > -1:
        print('A maior que B')
        par_impar()
    elif b > a and a > -1 and b > -1:
        print('B maior que A')
        par_impar()
    elif a < 0 or b < 0:
        print('digite somente numeros positivos'.capitalize())

    elif a == b:
        print('numeros iguais'.capitalize())
        par_impar()

# capitalize() deixa a primeira letra maiuscula

def par_impar():
    if a % 2 == 0 and b % 2 == 0:
        print('A e B são pares')
    elif a % 2 == 0 and not b % 2 == 0:
        print('A é par e B é impar')
    elif b % 2 == 0 and not a % 2 == 0:
        print('B é par e A é impar')
    else:
        print('A e B são impares')

verifica()