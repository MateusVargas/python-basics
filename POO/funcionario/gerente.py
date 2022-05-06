from funcionario import Funcionario

class Gerente(Funcionario):

    def __init__(self,nome,cpf,salario,senha,qtd_funcionarios):
        #Funcionario.__init__(nome,cpf,salario)
        super().__init__(nome,cpf,salario)#outra maneira de chamar os atributos da classe mãe
        self._senha = senha
        self._qtd_funcionarios = qtd_funcionarios
    
    def autenticar(self,senha):
        if self._senha == senha:
            print('Acesso permitido')
            return True
        else:
            print('Acesso negado')
            return False
    
    def get_bonificacao(self):
        return self._salario * 1.15