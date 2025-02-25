from datetime import datetime


clientes = []
numConta = 1
agencia = "0001"


def cadastroCliente():
    global clientes

    nome = input("Insira seu nome: ")
    dataNasc_str = input("Insira sua data de nascimento (DD/MM/AAAA): ")

    
    try:
        dataNasc = datetime.strptime(dataNasc_str, "%d/%m/%Y").date()
    except ValueError:
        print("Formato de data inválido! Use DD/MM/AAAA.")
        return

    cpf = input("Insira seu CPF (Apenas números): ")
    endereco = input("Insira seu endereço: ")

    
    for c in clientes:
        if c['cpf'] == cpf:
            print('CPF já cadastrado!')
            return

    cliente = {
        'nome': nome,
        'dataNasc': dataNasc,
        'cpf': cpf,
        'endereco': endereco,
        'contas': []  
    }

    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")


def cadastroConta():
    global numConta

    cpf = input("Informe o CPF do cliente para criar uma conta: ")
    
   
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            nova_conta = {
                "agencia": agencia,
                "numero": str(numConta).zfill(4),  # Mantém o formato 0001, 0002...
                "saldo": 0,
                "extrato": []
            }
            cliente["contas"].append(nova_conta)
            numConta += 1
            print(f"Conta {nova_conta['numero']} criada com sucesso para {cliente['nome']}!")
            return

    print("Erro: Cliente não encontrado!")

def exibir_extrato():
    cpf = input("Informe o CPF do cliente: ")

    for cliente in clientes:
        if cliente["cpf"] == cpf:
            print(f"\nContas do cliente {cliente['nome']}:\n")
            for conta in cliente["contas"]:
                print(f"Conta {conta['numero']} - Saldo: R${conta['saldo']:.2f}")

            conta_escolhida = input("Digite o número da conta para ver o extrato: ")

            for conta in cliente["contas"]:
                if conta["numero"] == conta_escolhida:
                    print("\n===== EXTRATO =====")
                    if not conta["extrato"]:
                        print("Nenhuma movimentação registrada.")
                    else:
                        for mov in conta["extrato"]:
                            print(mov)
                    print(f"\nSaldo atual: R${conta['saldo']:.2f}")
                    print("===================\n")
                    return

            print("Erro: Conta não encontrada!")
            return

    print("Erro: Cliente não encontrado!")


def depositar():
    cpf = input("Informe o CPF do cliente: ")

    for cliente in clientes:
        if cliente["cpf"] == cpf:
            print(f"\nContas do cliente {cliente['nome']}:\n")
            for conta in cliente["contas"]:
                print(f"Conta {conta['numero']} - Saldo: R${conta['saldo']:.2f}")

            conta_escolhida = input("Digite o número da conta para depositar: ")

            for conta in cliente["contas"]:
                if conta["numero"] == conta_escolhida:
                    try:
                        valor = float(input("Quanto deseja depositar? "))
                        if valor > 0:
                            conta["saldo"] += valor
                            conta["extrato"].append(f"+ R${valor:.2f}")
                            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
                        else:
                            print("Erro: O valor deve ser maior que zero.")
                    except ValueError:
                        print("Erro: Digite um valor numérico válido.")
                    return

            print("Erro: Conta não encontrada!")
            return

    print("Erro: Cliente não encontrado!")


def sacar():
    cpf = input("Informe o CPF do cliente: ")

    for cliente in clientes:
        if cliente["cpf"] == cpf:
            print(f"\nContas do cliente {cliente['nome']}:\n")
            for conta in cliente["contas"]:
                print(f"Conta {conta['numero']} - Saldo: R${conta['saldo']:.2f}")

            conta_escolhida = input("Digite o número da conta para sacar: ")

            for conta in cliente["contas"]:
                if conta["numero"] == conta_escolhida:
                    try:
                        valor = float(input("Quanto deseja sacar? "))

                        if 0 < valor <= conta["saldo"]:
                            conta["saldo"] -= valor
                            conta["extrato"].append(f"- R${valor:.2f}")
                            print(f"Saque de R${valor:.2f} realizado com sucesso!")
                        else:
                            print("Erro: Saldo insuficiente ou valor inválido.")
                    except ValueError:
                        print("Erro: Digite um valor numérico válido.")
                    return

            print("Erro: Conta não encontrada!")
            return

    print("Erro: Cliente não encontrado!")

# Menu principal
def menu():
    while True:
        print(f"""
        Banco do João
        ===================================
        Selecione uma das opções:
        1 - Cadastrar Cliente
        2 - Criar Conta
        3 - Depositar
        4 - Sacar
        5 - Visualizar Extrato
        0 - Sair
        ===================================
        """)

        opcao = input("Digite um número: ")

        if opcao == "1":
            cadastroCliente()
        elif opcao == "2":
            cadastroConta()
        elif opcao == "3":
            depositar()
        elif opcao == "4":
            sacar()
        elif opcao == "5":
            exibir_extrato()
        elif opcao == "0":
            print("Obrigado por usar o Banco do João. Até mais!")
            break
        else:
            print("Erro: Opção inválida! Escolha uma opção entre 0 e 5.")


menu()
