def conta_letras(lista):
    contador = []
    for i in lista:
        qtd = len(i)
        contador.append(qtd)
    return contador

def teste():
    return 5

if __name__ == "__main__":
    lista = ['casa','papel']
    print(conta_letras(lista))

