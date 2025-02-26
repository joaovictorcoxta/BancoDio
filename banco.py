from datetime import datetime

class Historico:
    def __init__(self):
        self.transacoes = []
    
    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)


class Transacao:
    def registrar(self, conta):
        raise NotImplementedError("Método deve ser implementado na subclasse")


class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor
    
    def registrar(self, conta):
        if self.valor > 0:
            conta.saldo += self.valor
            conta.historico.adicionar_transacao(f"Depósito de R${self.valor:.2f}")
            return True
        return False


class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor
    
    def registrar(self, conta):
        if 0 < self.valor <= conta.saldo:
            conta.saldo -= self.valor
            conta.historico.adicionar_transacao(f"Saque de R${self.valor:.2f}")
            return True
        return False


class Conta:
    def __init__(self, cliente, numero, agencia="0001"):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    def saldo(self):
        return self.saldo

    def sacar(self, valor):
        transacao = Saque(valor)
        return transacao.registrar(self)

    def depositar(self, valor):
        transacao = Deposito(valor)
        return transacao.registrar(self)


class ContaCorrente(Conta):
    def __init__(self, cliente, numero, limite, limite_saques):
        super().__init__(cliente, numero)
        self.limite = limite
        self.limite_saques = limite_saques


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        return transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento


clientes = []
num_conta = 1

def cadastrar_cliente():
    global clientes
    nome = input("Nome: ")
    cpf = input("CPF: ")
    data_nasc = input("Data de nascimento (DD/MM/AAAA): ")
    endereco = input("Endereço: ")
    
    if any(c.cpf == cpf for c in clientes):
        print("Erro: CPF já cadastrado!")
        return
    
    cliente = PessoaFisica(nome, cpf, datetime.strptime(data_nasc, "%d/%m/%Y").date(), endereco)
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")


def criar_conta():
    global num_conta
    cpf = input("Informe o CPF do cliente: ")
    cliente = next((c for c in clientes if c.cpf == cpf), None)
    
    if not cliente:
        print("Erro: Cliente não encontrado!")
        return
    
    conta = Conta(cliente, str(num_conta).zfill(4))
    cliente.adicionar_conta(conta)
    num_conta += 1
    print(f"Conta {conta.numero} criada com sucesso!")


def depositar():
    cpf = input("Informe o CPF do cliente: ")
    cliente = next((c for c in clientes if c.cpf == cpf), None)
    
    if not cliente:
        print("Erro: Cliente não encontrado!")
        return
    
    if not cliente.contas:
        print("Erro: Cliente não possui conta cadastrada!")
        return
    
    valor = float(input("Valor do depósito: "))
    conta = cliente.contas[0]
    if conta.depositar(valor):
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    else:
        print("Erro ao depositar!")


def sacar():
    cpf = input("Informe o CPF do cliente: ")
    cliente = next((c for c in clientes if c.cpf == cpf), None)
    
    if not cliente:
        print("Erro: Cliente não encontrado!")
        return
    
    if not cliente.contas:
        print("Erro: Cliente não possui conta cadastrada!")
        return
    
    valor = float(input("Valor do saque: "))
    conta = cliente.contas[0]
    if conta.sacar(valor):
        print(f"Saque de R${valor:.2f} realizado com sucesso!")
    else:
        print("Erro ao sacar!")


def exibir_extrato():
    cpf = input("Informe o CPF do cliente: ")
    cliente = next((c for c in clientes if c.cpf == cpf), None)
    
    if not cliente:
        print("Erro: Cliente não encontrado!")
        return
    
    if not cliente.contas:
        print("Erro: Cliente não possui conta cadastrada!")
        return
    
    conta = cliente.contas[0]
    print("\n===== EXTRATO =====")
    for transacao in conta.historico.transacoes:
        print(transacao)
    print(f"\nSaldo atual: R${conta.saldo:.2f}")
    print("===================\n")


def menu():
    while True:
        print("""
        Banco do João
        1 - Cadastrar Cliente
        2 - Criar Conta
        3 - Depositar
        4 - Sacar
        5 - Extrato
        0 - Sair
        """)
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            criar_conta()
        elif opcao == "3":
            depositar()
        elif opcao == "4":
            sacar()
        elif opcao == "5":
            exibir_extrato()
        elif opcao == "0":
            print("Obrigado por usar o Banco do João!")
            break
        else:
            print("Opção inválida!")

menu()
