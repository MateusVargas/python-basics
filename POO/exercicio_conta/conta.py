from historico import Historico

class Conta:

    __slots__ = ['_numero','_titular','_saldo','_limite','historico']
    #__slots__ atribui um numero fixo de atributos para a classe, não permitindo que sejam
    #criados novos atributos em tempo de execução por exemplo

    _total_contas = 0

    def __init__(self,numero,saldo,titular,limite=20000):
        self._numero = numero
        self._saldo = saldo #'_saldo' alerta que o atributo não deve ser acessado diretamente fora da classe!, '__saldo' torna o atributo privado
        self._titular = titular
        self._limite = limite
        self.historico = Historico()
        type(self)._total_contas += 1

    @classmethod #metodo da classe
    def get_total_contas(cls):#cls é um objeto do tipo class, uma referencia da classe
        return cls._total_contas
    
    def deposita(self, valor):
        if valor > self._limite:
            print('\nLimite excedido!\n\n')
            return False
        else:
            self._saldo += valor
            #print('Saldo após deposito: ',self._saldo)
            self.historico.transacoes.append('Depósito de R$:{}'.format(valor))
    
    def sacar(self, valor):
        if self._saldo < valor:
            print('\nSaldo insuficiente para realizar o saque!\n\n')
            return False
        elif valor > self._limite:
            print('\nLimite excedido!')
            return False
        else:
            self._saldo -= valor
            self.historico.transacoes.append('Saque de R$: {}'.format(valor))


    def extrato(self):
        print('****EXTRATO****\nNumero: {}\nSaldo: {}\nTitular: {}\n\n'.format(self._numero,self._saldo,self._titular.nome+' '+self._titular.sobrenome))
        self.historico.transacoes.append('retirou extrato - saldo de R$: {}'.format(self._saldo))
    
    def transfere_para(self, destino, valor):
        retirou = self.sacar(valor)
        if retirou == False:
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append('Transferência de R$: {} para a Conta: {}'.format(valor, destino._numero))
            return True