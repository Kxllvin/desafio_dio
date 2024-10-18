import textwrap

def menu():
    menu = """

        [nu] Novo Usuário
        [nc] Nova Conta
        [lc] Listar Contas
        [d] Deposito
        [s] Saque
        [e] Extrato
        [q] Sair

    =>"""
    return input(textwrap.decent(menu))


def depositar(saldo, valor, extrato):
    print("Depósito".center(14))
    if valor > 0:
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f} Realizado.\n"
            print(extrato)
        
    else:
        print("O valor informado não é válido")
    
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saque, LIMITE_SAQUE):
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
    
    else:
        print("Operação Falhou! Foi excedido limite de saques")
    
    return saldo, extrato


def exibe_extrato(saldo, /, *, extrato):
    print("Extrato".center(14))
            # Exibe o extrato, ou uma mensagem se não houver transações
    if not extrato:
        #print("Não foram realizadas movimentações.")
        print("Não foram realizadas movimentações." if not extrato else extrato)
    else:
        print(f"Saldo atual: R$ {saldo:.2f}")
    

def cadastro_usuario(usuarios):
    cpf = input("Informe os número do CPF: ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("Já existe um usuário com este CPF!")
        return
    
    nome = input("Nome completo: ")
    data_nasc = input("Data de Nascimento: ")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nasc": data_nasc, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, num_conta, usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta Criada com sucesso!")
        return {"agencia": agencia, "num_conta": num_conta, "usuario": usuario}

    print("Usuário não encontrado, criação de conta encerrada!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: {conta['agencia']}
            C/C: {conta['num_conta']}
            Titular: {conta['usuario']['nome']}
        """
        print(textwrap.decent(linha))

def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0123"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saque = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Qual valor deseja depositar? =>"))

            saldo, extrato = depositar(saldo, valor, extrato)

            
        elif opcao == "s":
            valor = float(input("Qual valor deseja depositar? =>"))
            
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saque=numero_saque,
                limite_saque=LIMITE_SAQUE,
            )
                
        elif opcao == "e":
            exibe_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            cadastro_usuario(usuarios)

        elif opcao == "nc":
            num_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, num_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("Saindo...".center(14))
            break

        else:
            print("Opção inválida, por favor selecione novamente a operação desejada.")

main()