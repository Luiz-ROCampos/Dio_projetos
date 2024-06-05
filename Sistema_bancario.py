saldo = 0 
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3
numero_conta = 1
AGENCIA = '0001'
usuarios = []
contas = []

def depositar(saldo, extrato, /):
    deposito = int(input("Digite o valor de depósito: \n R$ "))
    if deposito <= 0:
        print("Valor incorreto!")
    else:
        saldo += deposito
        extrato += f"Deposito:      R$ {deposito:.2f}\n"
        print("\nDeposito Realizado com Sucesso!")
    return saldo, extrato

def sacar(saldo, extrato, numero_saque, / , limite_saque = LIMITE_SAQUE):
    if numero_saque >= limite_saque:
        print("O limite de saque foi atingido, tente sacar amanhã.")
    else:
        saque = int(input("Digite o valor de saque: \n R$ "))

    if saque <= 0:
        print("Valor incorreto!")
    elif saque > saldo:
        print("\nSeu saldo é insuficiente para realizar o saque.")
    else:
        saldo -= saque
        extrato += f"Saque:         R$ {saque:.2f}"
        numero_saque += 1
        print("\nSaque realizado com sucesso!")
    return saldo, extrato, numero_saque

def visualizar_extrato(saldo, /, *, extrato):
    print("""
----------------------------------- 
        Extrato Bancário
----------------------------------- 
""")
    if extrato == "" :
        print("Não houve movimentações")
    else:
        print(extrato)
        print(f"\nSaldo atual:   R$ {saldo:.2f}")

def novo_usuario(usuarios):
    cpf = input("Digite seu CPF: \n")
    if filtrar_usuario(cpf, usuarios):
        print("Usuário cadastrado!")
        return
    nome = input("Digite seu nome: \n")
    data_nascimento = input("Digite sua data de nascimento: \n")
    endereco = input("digite seu endereco: \n")
    usuarios.append({"nome": nome, "CPF": cpf, "data_nascimento": data_nascimento, "endereco": endereco})

    return usuarios
     
def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["CPF"] == cpf:
            return True    
    return False

def criar_conta(contas, usuarios, AGENCIA, numero_conta):
    cpf = input("Digite seu CPF: \n")
    if filtrar_usuario(cpf, usuarios):
        print("Usuário não cadastrado!")
        return
    agencia = AGENCIA
    numero_conta += 1
    contas.append({"agencia": agencia, "numero_conta": numero_conta, "CPF": cpf})
    print("Conta criada com sucesso!")
    return contas


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
        saldo, extrato = depositar(saldo, extrato)
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
