lista = [45, 0, 4, 8]
lista_palavras = ['gato','casa','aviao','limão']

print(lista_palavras[3])
print('Soma dos elementos da lista: ',sum(lista))
print('Maior valor da lista: ',max(lista))
print('Menor valor da lista: ',min(lista))
print('Maior valor da lista de palavras: ',max(lista_palavras))
print('Menor valor da lista de palavras: ',min(lista_palavras))

#min e max em strings retornam maior e menor valor com base na letra inicial da palavra

for i in lista_palavras:
    print(i)

#procurando valor em uma lista:
if 'gato' in lista_palavras:
    print('existe')
else:
    print('não existe')
    lista_palavras.append('gato')

if 87 in lista:
    print('existe')
else:
    print('não existe')
    lista.append(87)
    print(lista)

lista.pop() # retirando o ultimo elemento
lista_palavras.pop(1) # apagando elemento na posição 1
lista_palavras.remove('aviao') # retirando o elemento pelo nome

#duplicando os valores da lista
nova_lista = lista_palavras * 2
print(nova_lista)

nova_lista.sort() # ordenando a lista
print(nova_lista)

nova_lista.reverse() # ordenando de trás pra frente
print(nova_lista)


print(len(nova_lista)) # retornando tamanho

#TUPLAS: são elementos que não podem ser mudados
tupla = (5,8,3,44)
print(tupla)
print(tupla[2])

tupla_palavras = tuple(lista_palavras) # convertendo lista em tupla
print(tupla_palavras)

lista_numeros = list(tupla) # convertendo tupla em lista
print(lista_numeros)
