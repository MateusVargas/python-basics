n1 = float(input('Nota 1: '))
while n1 > 10:
    n1 = float(input('Nota inválida. Nota 1: '))

n2 = float(input('Nota 2: '))
while n2 > 10:
    n2 = float(input('Nota inválida. Nota 2: '))

media = (n1 + n2) / 2
print('media: {}'.format(media))