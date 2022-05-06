conjunto = {1,4,4,7,9,3}
conjunto2 = {6,7,9,11,1}

print(conjunto)

conjunto.add(8) # adicionando elemento
conjunto.discard(7) # removendo elemento
print(conjunto)

conjunto_uniao = conjunto.union(conjunto2) # unindo conjuntos
print('União: {}'.format(conjunto_uniao))

conjunto_interseccao = conjunto.intersection(conjunto2) # interseccao de conjuntos
print('Intersecção: {}'.format(conjunto_interseccao))

conjunto_diferenca = conjunto.difference(conjunto2) # diferenca entre conjuntos(elementos que exitem em um, e não existem no outro conjunto)
print('Diferença: {}'.format(conjunto_diferenca))

conjunto_diferenca_simetrica = conjunto.symmetric_difference(conjunto2)
# diferenca simetrica: os elementos que não existem em ambos os conjuntos
print('Diferença simétrica: {}'.format(conjunto_diferenca_simetrica))


conjunto_a = {1,7,4}
conjunto_b = {1,4,3,7}
conjunto_sub = conjunto_a.issubset(conjunto_b) # retorna true se conjunto 'a' for um subconjunto de 'b'
print(conjunto_sub)

conjunto_super = conjunto_b.issuperset(conjunto_a) # retorna true se conjunto 'b' é um superconjunto de 'a'
print(conjunto_super)

lista = ['casa','cor','gato','telefone','telefone']
conjunto_palavras = set(lista) # convertendo lista em conjunto pra eliminar a duplicidade
print(conjunto_palavras)

lista2 = list(conjunto_palavras) # converter conjunto em lista
print(lista2)