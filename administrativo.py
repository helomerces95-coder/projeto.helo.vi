from cliente import Cliente

class Administrador(Pessoa):   #classe adm vai herdar de pessoa
    def __init__(self, nome, cpf, idade):
        super().__init__(nome, cpf, idade):
        