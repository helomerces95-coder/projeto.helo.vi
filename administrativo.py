from cliente import Cliente

class Administrador(Pessoa):   #classe adm vai herdar de pessoa
    def __init__(self, nome, cpf, idade):
        super().__init__(nome, cpf, idade):
        self.clientes = []

def cancelar_agendamento(self, cliente: Cliente):
        cliente.agendamento = None
        cliente.procedimento = None
        cliente.forma_pagamento = None
        print(f"Agendamento de {cliente.nome} cancelado.")

def historico_tratamentos(self, cliente: Cliente):
        print(f"Histórico de tratamentos de {cliente.nome}: {cliente.procedimento if cliente.procedimento else 'Nenhum tratamento realizado.'}")

def faturamento(self, cliente: Cliente):
        print(f"Forma de pagamento de {cliente.nome}: {cliente.forma_pagamento if cliente.forma_pagamento else 'Não definido'}")
