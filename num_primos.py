numero = int(input('Digite um numero: '))
total = 0

for i in range(1, numero+1):
    if numero % i == 0:
        total += 1
if total == 2:
    print(numero,'É primo')
else:
    print(numero,'Não é primo')


numero = int(input('Contar números primos de 1 até ?: '))
for i in range(numero+1):
    total = 0
    for j in range(1, i+1):
        if i % j == 0:
            total += 1
    if total == 2:
        print(i)