menu = ''' 
----------------------------------- 
     Bem vindos ao banco futuro 
----------------------------------- 
selecione uma opÃ§Ã£o: 
[1] Deposito 
[2] Saque 
[3] Extrato 
[0] Sair 
----------------------------------- ''' 
saldo = 100 
extrato = ''' 
----------------------------------- 
              Extrato 
----------------------------------- 

Valores de Saque R$ {}. 
Valores de DepÃ³sito R$ {}. 
Saldo atualizado R$ {}. ''' 
numero_saque = 0 
LIMITE_SAQUE = 3 
valores_saque = [] 
valores_deposito = [] 
while True: 
    opcao = int(input(menu))
    if opcao == 1:
        deposito = int(input("Digite o valor de depósito: \n R$ "))
        if deposito >= 0:
            print("Valor incorreto!")
        else:
            saldo += deposito
            valores_deposito.append(deposito)
    elif opcao == 2:
        if numero_saque >= LIMITE_SAQUE:
            print("O limite de saque foi atingido, tente sacar amanhÃ£.")
        else:
            saque = int(input("Digite o valor de saque: \n R$ "))
            if saque <= 0:
                print("Valor incorreto!")
            elif saque > 0:
                saldo -= saque
                valores_saque.append(saque)
                numero_saque += 1
            else:
                print("Seu saldo é insuficiente para realizar o saque.")
    elif opcao == 3:
        print(extrato.format(valores_saque, valores_deposito, saldo))
    elif opcao == 0:
        print("Obrigado por nos visitar!")
    else:
        print("Opção inválida")
