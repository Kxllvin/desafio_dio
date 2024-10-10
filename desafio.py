menu = """

    [d] Deposito
    [s] Saque
    [e] Extrato
    [q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito".center(14))

        valor = float(input("Qual valor deseja depositar? =>"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f} Realizado.\n"
            print(extrato)
        
        else:
            print("O valor informado não é válido")

    elif opcao == "s":
        print("Saque".center(14))

        valor = float(input("Qual valor deseja sacar? =>"))

        exceder_saldo = valor > saldo
        exceder_limite= valor > limite
        exceder_saque = numero_saque >= LIMITE_SAQUE

        if exceder_saldo:
            print("Operação Falhou! Saldo insuficiente")

        elif exceder_limite:
            print("Operação Falhou! O valor excede o limite disponível")

        elif exceder_saque:
            print("Operação Falhou! Foi excedido limite de saques")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque de R$ {valor:.2f}\n"
            numero_saque += 1
            print(extrato)
            
    elif opcao == "e":
        print("Extrato".center(14))
                # Exibe o extrato, ou uma mensagem se não houver transações
        if not extrato:
            #print("Não foram realizadas movimentações.")
            print("Não foram realizadas movimentações." if not extrato else extrato)
        else:
            print(extrato)

    elif opcao == "q":
        print("Saindo...".center(14))
        break

    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.")
