import random
from cliente import Cliente

class Pessoa:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade


class Administrador(Pessoa):  # Classe Administrador que herda de Pessoa
    def __init__(self, nome, cpf, idade):
        super().__init__(nome, cpf, idade)
        self.clientes = []

    # Função para cancelar agendamento
    def cancelar_agendamento(self, cliente: Cliente):
        cliente.agendamento = None
        cliente.procedimento = None
        cliente.forma_pagamento = None
        print(f"Agendamento de {cliente.nome} cancelado.")

    # Função para exibir histórico de tratamentos
    def historico_tratamentos(self, cliente: Cliente):
        print(f"Histórico de tratamentos de {cliente.nome}: {cliente.procedimento if cliente.procedimento else 'Nenhum tratamento realizado.'}")

    # Função para exibir forma de pagamento
    def faturamento(self, cliente: Cliente):
        print(f"Forma de pagamento de {cliente.nome}: {cliente.forma_pagamento if cliente.forma_pagamento else 'Não definido'}")

    # Função de editar agendamento
    def editar_agendamento(self, cliente: Cliente):
        if cliente.agendamento:
            print(f"\nAgendamento atual de {cliente.nome}: {cliente.agendamento} | {cliente.procedimento}")
            novo_procedimento = input("Digite o novo procedimento (ou deixe em branco para não alterar): ")
            if novo_procedimento:
                cliente.procedimento = novo_procedimento
            nova_data = input("Digite a nova data do agendamento (dd/mm/yyyy ou deixe em branco para não alterar): ")
            if nova_data:
                cliente.agendamento = nova_data
            nova_forma_pagamento = input("Digite a nova forma de pagamento (cartão/dinheiro/pix ou deixe em branco para não alterar): ")
            if nova_forma_pagamento:
                cliente.forma_pagamento = nova_forma_pagamento
            print(f"Agendamento de {cliente.nome} atualizado com sucesso!")
        else:
            print(f"{cliente.nome} não tem agendamento!")

    # Função de sorteio de cliente premiado
    def sortear_cliente_premiado(self, clientes):
        if clientes:
            cliente_premiado = random.choice(list(clientes.values()))
            print(f"Cliente premiado: {cliente_premiado.nome} ({cliente_premiado.cpf})!")
            print(f"Parabéns {cliente_premiado.nome}, você ganhou um benefício exclusivo!")
        else:
            print("Nenhum cliente cadastrado para sorteio.")
