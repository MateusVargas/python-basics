a = 67
b = 0
lista = [6,9]

try:
    divisao = a / 1
    numero = lista[1]
    x = a

except ZeroDivisionError: # passando o nome da excessão para tratar um erro especifico
    print('não e possivel dividir por zero')
except IndexError:
    print('elemento inexistente')
#except NameError:
#    print('variavel não existe')
#except BaseException as e: # excessão base, pai de todas as exceções
#    print(e)
except Exception as e:
    print('houve uma excessão',e)
except:
    print('excecão desconhecida')

else:#só será excutado se não houver exceções
    print('continua a execução')

finally:# bloco finally sempre será executado independente de erros
    print('sempre será executado')