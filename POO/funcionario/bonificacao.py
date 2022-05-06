from funcionario import Funcionario
from gerente import Gerente

class ControleBonificacao:

    def __init__(self, total_bonificacoes=0):
        self._total_bonificacoes = total_bonificacoes

    def registra(self, funcionario):#polimorfismo, foi passado um gerente onde se espera um funcionario, pois gerente herda de funcionario
        if(hasattr(funcionario,'get_bonificacao')):#verifica se o objeto recebido implementa o metodo get_bonificacao()
        #o metodo isinstance(obj, Funcionario) verifica se o objeto passado é uma instancia de Funcionario
            self._total_bonificacoes += funcionario.get_bonificacao()
        else:
            print('este objeto não implementa o método get_bonificacao')

    def total_bonificacoes(self):
        return self._total_bonificacoes
    

func = Funcionario('jose','555.900.672-00',890)
gerente = Gerente('joao','126.432.988-10',1000,'1234',4)
print('bonificação gerente: ',gerente.get_bonificacao())
print('bonificacao funcionario: ',func.get_bonificacao())
#print(vars(gerente))

controle = ControleBonificacao()
controle.registra(func)
controle.registra(gerente)
print('total: {}'.format(controle.total_bonificacoes()))