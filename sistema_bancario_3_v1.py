from datetime import datetime
from abc import abstractclassmethod, ABC

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Conta:
    def __init__(self, numero, cliente):
        self._cliente = cliente
        self._agencia = '0001'
        self._numero = numero
        self._saldo = saldo
        self._historico = Historico()

    def nova_conta(cls, numero, cliente ):
        return cls(numero, cliente)
    
    def saldo(self):
        return self._saldo
    
    def numero(self):
        return self._numero
    
    def agencia(self):
        return self._agencia
    
    def cliente(self):
        return self._cliente
    
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        
        if valor > 0:
            self._saldo -= valor
            print("Saque realizado com sucesso!")
            return True
        elif valor > 0:
            print("Seu saldo é insulficiente para realizar o saque.")
        else:
            print("Valor digitado inválido")

        return False
        
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Deposito realizado com sucesso!")
            return True
        else:
            print("Valor digitado inválido")

        return False
    
class ContaCorrente(Conta):
    def __init__(self,numero, cliente, limite = 400, limite_saques = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] = Saque.__name__])
        if valor > self.limite:
            print("Valor de saque superior ao limite diário.")
        elif numero_saques >= self.limite_saques:
            print("numero maximo de saque foi atingido!")
        else:
            return super().sacar(valor)
        
        return False  
    
    def __str__(self):
        return f"""\
            Agência:   {self.agencia}
            C/c:       {self.numero}
            Titular    {self.cliente.nome}
            """
    
class Historico:
    def __init__(self):
        self.transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strtime("%d/%m/%Y %H:%M:%s"),
            }
        )
    
class Transacao(ABC):
    @property
    @abstractclassmethod
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def sacar(self, valor):
        return self._valor 
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_historico(self)





menu = ''' 
----------------------------------- 
     Bem vindo ao banco futuro 
----------------------------------- 
selecione uma opção: 
[1] Deposito 
[2] Saque 
[3] Extrato
[4] Criar usuario
[5] Criar conta
[0] Sair 
-----------------------------------\n'''

while True: 
    opcao = int(input(menu))
    if opcao == 1:
        
    elif opcao == 2:
        saldo, extrato, numero_saque = sacar(saldo, extrato, numero_saque, limite_saque = LIMITE_SAQUE)
    elif opcao == 3:
        visualizar_extrato(saldo, extrato=extrato)
    elif opcao == 4:
        usuarios = novo_usuario(usuarios)
    elif opcao == 5:
        contas = criar_conta(usuarios, contas, AGENCIA, numero_conta)
    elif opcao == 0:
        print("Obrigado por nos visitar!")
        break
    else:
        print("Opção inválida")


