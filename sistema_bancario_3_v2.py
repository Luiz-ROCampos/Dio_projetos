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
        self._saldo = 0
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
    def __init__(self, numero, cliente, limite = 400, limite_saques = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
            )
        if valor > self.limite:
            print("Valor de saque superior ao limite diário.")
        elif numero_saques >= self.limite_saques:
            print("numero maximo de saque foi atingido!")
        else:
            return super().sacar(valor)
        
        return False  
    
    def __str__(self):
        return f"""\n
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

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
        if not cliente.conta:
            print("Cliente não possue conta")
            return
        return cliente.contas[0]

def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado")
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    valor = float(input("Informe o valor de deposito: R$ "))
    transacao = Deposito(valor)
    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")

    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("Cliente não encontrado")
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    valor = float(input("Informe o valor de saque: R$ "))
    transacao = Saque(valor)
    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")

    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("Cliente não encontrado")

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print("""
          \n-----------------------------------
                          EXTRATO             
            -----------------------------------
            """)
    transacao = conta.historico.transacoes

    extrato = ''

    if not transacao:
        extrato += 'Não foram encontrado movimentações'
    else:
        for transacao in transacoes:
            extrato += f'\n{transacao['tipo']}:\t\t{transacao['valor']:.2f}'

    print(extrato)
    print(f'\nSaldo:\t\tR$ {conta.saldo:.2f}')
    print('-----------------------------------')

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o cpf do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("Cliente não encontrado")
        return
    
    conta = ContaCorrente.nova_conta(numero=numero_conta, cliente=cliente)
    contas.append(conta)
    cliente.contas.append(conta)

    print('Conta Criada com sucesso!')

def criar_cliente(clientes):
    cpf = input('Informe o CPF: ')
    cliente = filtrar_cliente(cpf, clientes)
    if cliente:
        print("Já existe um cliente cadastrado com esse CPF!")
        return
    nome = input("Digite seu nome: ")
    data_nascimento = input("Digite sua data de nascimento: ")
    endereco = input("Digite seu endereço: ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(cliente)


clientes = []
contas = []

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
        depositar(clientes)
    elif opcao == 2:
        sacar(clientes)
    elif opcao == 3:
        exibir_extrato(clientes)
    elif opcao == 4:
        criar_cliente(clientes)
    elif opcao == 5:
        numero_conta = len(contas) + 1
        criar_conta(numero_conta, clientes, contas)
    elif opcao == 0:
        print("Obrigado por nos visitar!")
        break
    else:
        print("Opção inválida")
