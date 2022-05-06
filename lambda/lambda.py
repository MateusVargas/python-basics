# lambda são funções anônimas, não precisa colocar nome nesse tipo de função
contador_letras = lambda lista: [len(i) for i in lista] 
#lambda é bom para pequenas funções

lista = ['gato', 'cachorro']
print(contador_letras(lista))

soma = lambda a, b: a + b
divisao = lambda a, b: a / b
print(soma(34,880))
print(divisao(3,6))

calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b
}# dicionario de funções anônimas

soma = calculadora['soma']
multi = calculadora['multiplicacao']
print(soma(5,8))
print(multi(2,9))