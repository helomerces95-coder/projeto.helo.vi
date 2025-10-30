class Procedimento:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return self.nome

class Procedimentofacial(Procedimento):
    def __init__(self, nome, preco):
        super().__init__(nome, preco)

class LimpezaDePele(Procedimentofacial):
    def __init__(self):
        super().__init__("Limpeza de Pele", 200)

class Botox(Procedimentofacial):
    def __init__(self):
        super().__init__("Botox", 600)

class Tratamentoacne(Procedimentofacial):
    def __init__(self, nome, preco):
        super().__init__(Acne, preco)
    
class ProcedimentoCorporal(Procedimento):
    def __init__(self, nome, preco):
        super().__init__(nome, preco)