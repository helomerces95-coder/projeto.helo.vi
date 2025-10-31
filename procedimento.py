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

class TratamentoAcne(Procedimentofacial):
    def __init__(self):
        super().__init__("Tratamento para Acne", 300)

class ProcedimentoCorporal(Procedimento):
    def __init__(self, nome, preco):
        super().__init__(nome, preco)

class Drenagem(ProcedimentoCorporal):
    def __init__(self):
        super().__init__("Drenagem", 150)

class MassagemModeladora(ProcedimentoCorporal):
    def __init__(self):
        super().__init__("Massagem Modeladora", 180)

class TratamentoEstrias(ProcedimentoCorporal):
    def __init__(self):
        super().__init__("Tratamento de Estrias", 250)

# Procedimentos Capilares
class ProcedimentoCapilar(Procedimento):
    def __init__(self, nome, preco):
        super().__init__(nome, preco)

class TratamentoQueda(ProcedimentoCapilar):
    def __init__(self):
        super().__init__("Tratamento para Queda Capilar", 300)

class HidrataçãoCapilar(ProcedimentoCapilar):
    def __init__(self):
        super().__init__("Hidratação Capilar", 200)
