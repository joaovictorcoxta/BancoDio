deposito = 0
saque = 0
saldo = 0
extrato_deposito = []
extrato_saque = []
lim_saque = 0  

def menu():
    print(f"""
    Banco do João
    ===================================
        Selecione uma das opções:
        1 - Depositar
        2 - Sacar
        3 - Visualizar extrato
        0 - Sair
    ===================================
    """)

def depositar(valor):
    global saldo
    if valor > 0:
        saldo += valor
        extrato_deposito.append(valor)
        print(f"O valor de R${valor:.2f} foi depositado com sucesso!")
    else:
        print("Erro: O valor do depósito deve ser maior que zero.")

def sacar(valor):
    global saldo, lim_saque

    if lim_saque >= 3:
        print("Erro: Limite de saques diários atingido (máximo de 3).")
        return

    if 0 < valor <= saldo:
        if valor <= 500:
            saldo -= valor
            lim_saque += 1
            extrato_saque.append(valor)
            print(f"R$ {valor:.2f} sacado com sucesso!")
        else:
            print("Erro: O limite por saque é de R$500.")
    else:
        print("Erro: Saldo insuficiente ou valor inválido.")

def exibir_extrato():
    print("\n===== EXTRATO =====")
    if not extrato_deposito and not extrato_saque:
        print("Nenhuma movimentação registrada.")
    else:
        print("\nDepósitos:")
        for dep in extrato_deposito:
            print(f"  + R${dep:.2f}")

        print("\nSaques:")
        for saq in extrato_saque:
            print(f"  - R${saq:.2f}")
    
    print(f"\nSaldo atual: R${saldo:.2f}")
    print("===================\n")


while True:
    menu()
    opcao = input("Digite um número: ")

    if opcao == "1":
        try:
            valor = float(input("Quanto você deseja depositar? "))
            depositar(valor)
        except ValueError:
            print("Erro: Digite um valor numérico válido.")

    elif opcao == "2":
        try:
            valor = float(input("Quanto você deseja sacar? "))
            sacar(valor)
        except ValueError:
            print("Erro: Digite um valor numérico válido.")

    elif opcao == "3":
        exibir_extrato()

    elif opcao == "0":
        print("Obrigado por usar o Banco do João. Até mais!")
        break

    else:
        print("Erro: Opção inválida! Escolha uma opção entre 0 e 3.")


            
