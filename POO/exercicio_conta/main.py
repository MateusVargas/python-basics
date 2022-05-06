from conta import Conta
from cliente import Cliente

if __name__ == "__main__":
    cliente = Cliente('Jonas','Silva','123.456.789-00')
    cliente2 = Cliente('Félix','Da Costa','455.900.677-55')
    cliente3 = Cliente('Diego','Ribas','433.699.123-55')

    conta = Conta('592-0',3900,cliente,12000)
    conta2 = Conta('4338-8',1222.78,cliente2,6000)

    #conta._Conta__saldo=2000 => acessando o atributo privado(não deve ser acessado diretamente)
    conta.deposita(190)
    conta.transfere_para(conta2, 400)
    conta.historico.imprime()
    conta.extrato()


    conta2.deposita(60000)
    conta2.sacar(8000)
    conta2.historico.imprime()
    conta2.extrato()
    c2 = conta2 #c2 está apontando para o mesmo endereço de memória
    #que conta2, portanto apontando pro mesmo objeto, o valor de c2 não é o
    #objeto e sim o endereço de memória
    #c2.extrato()


    conta3 = Conta('225-90',5000,cliente3,30000)
    #print('\ntitular da conta 3: {}'.format(conta3.titular.nome))
    conta3.deposita(2300)
    conta3.sacar(200)
    conta3.historico.imprime()
    conta3.extrato()

    print('total de contas: ',Conta.get_total_contas())
