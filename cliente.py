import json

class Pessoa():   # classe base
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade =idade

class Cliente(Pessoa):   # vai herdar da classe pessoa
    def __init__(self, nome, cpf, idade, telefone, email, agendamento=None, procedimento=None, forma_pagamento=None, orientacoes=None):
        super().__init__(nome, cpf, idade)
        self.telefone = telefone
        self.email = email
        self.agendamento = agendamento
        self.procedimento = procedimento
        self.forma_pagamento = forma_pagamento
        self.orientacoes = orientacoes

    def agendar_procedimento(self, data, procedimento, forma_pagamento):
        self.agendamento = data
        self.procedimento = procedimento
        self.forma_pagamento = forma_pagamento
        print(f"\n✅ Agendamento feito com sucesso para {self.nome} em {data}.\n")

    def carregar_dados():
        try:
            with open('data.json', 'r') as f:
                return json.load(f)
        except: FileNotFoundError
        return{}
                
    def salvar_dados(dados):
        with open('data.json', 'w') as f:
            json.dump(dados, f, indent=4)