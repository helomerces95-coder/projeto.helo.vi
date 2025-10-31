from cliente import Cliente, carregar_dados, salvar_dados
from administrativo import Administrador
from procedimento import LimpezaDePele, Botox, TratamentoAcne, Drenagem, MassagemModeladora, TratamentoEstrias, TratamentoQueda, HidrataçãoCapilar

# Função de menu
def menu():
    print("\n=== CLÍNICA ESTÉTICA JK ===")
    print("1. Cadastro de Cliente")
    print("2. Agendar Procedimento")
    print("3. Cancelar Agendamento (ADM)")
    print("4. Histórico de Tratamentos (ADM)")
    print("5. Faturamento (ADM)")
    print("6. Editar agendamento")
    print("7. Sorteio de Cliente Premiado (ADM)")
    print("8. Sair")

# Função para cadastro de cliente
def cadastro_cliente():
    print("\n--- Cadastro de Novo Cliente ---")
    nome = input("Nome completo: ")
    cpf = input("CPF: ")
    idade = input("Idade: ")
    telefone = input("Telefone (com DDD): ")
    email = input("E-mail: ")

    cliente = Cliente(nome, cpf, idade, telefone, email)
    print(f"\n✅ Cliente {nome} cadastrado com sucesso!\n")
    return cliente

# Função para agendar procedimento
def agendar_cliente(clientes):
    cpf_cliente = input("Digite o CPF do cliente: ")
    if cpf_cliente in clientes:
        cliente = clientes[cpf_cliente]
        print("\nEscolha uma categoria de procedimento:")
        print("1. Procedimentos Faciais")
        print("2. Procedimentos Corporais")
        print("3. Procedimentos Capilares")
       
        escolha_categoria = input("Digite o número da categoria: ")

        if escolha_categoria == '1':
            procedimentos_faciais(cliente)
        elif escolha_categoria == '2':
            procedimentos_corporais(cliente)
        elif escolha_categoria == '3':
            procedimentos_capilares(cliente)
        else:
            print("Opção inválida!")
    else:
        print("\nCliente não encontrado.")

# Procedimentos faciais
def procedimentos_faciais(cliente):
    print("\n--- Procedimentos Faciais ---")
    print("1. Limpeza de Pele")
    print("2. Botox")
    print("3. Tratamento para Acne")

    escolha = input("Escolha o número do procedimento: ")
    procedimentos = {
        "1": LimpezaDePele(),
        "2": Botox(),
        "3": TratamentoAcne()
    }

    procedimento = procedimentos.get(escolha)
    if not procedimento:
        print("Procedimento inválido!")
        return

    data = input("Data do agendamento (dd/mm/yyyy): ")
    forma_pagamento = input("Forma de pagamento (cartão/dinheiro/pix): ")

    cliente.agendar_procedimento(data, procedimento.nome, forma_pagamento)
    orientacoes = input("Orientações pós-procedimento: ")
    cliente.definir_orientacoes(orientacoes)

# Procedimentos corporais
def procedimentos_corporais(cliente):
    print("\n--- Procedimentos Corporais ---")
    print("1. Drenagem")
    print("2. Massagem Modeladora")
    print("3. Tratamento de Estrias")

    escolha = input("Escolha o número do procedimento: ")
    procedimentos = {
        "1": Drenagem(),
        "2": MassagemModeladora(),
        "3": TratamentoEstrias()
    }

    procedimento = procedimentos.get(escolha)
    if not procedimento:
        print("Procedimento inválido!")
        return

    data = input("Data do agendamento (dd/mm/yyyy): ")
    forma_pagamento = input("Forma de pagamento (cartão/dinheiro/pix): ")

    cliente.agendar_procedimento(data, procedimento.nome, forma_pagamento)
    orientacoes = input("Orientações pós-procedimento: ")
    cliente.definir_orientacoes(orientacoes)

# Procedimentos capilares
def procedimentos_capilares(cliente):
    print("\n--- Procedimentos Capilares ---")
    print("1. Tratamento para Queda Capilar")
    print("2. Hidratação Capilar")

    escolha = input("Escolha o número do procedimento: ")
    procedimentos = {
        "1": TratamentoQueda(),
        "2": HidrataçãoCapilar()
    }

    procedimento = procedimentos.get(escolha)
    if not procedimento:
        print("Procedimento inválido!")
        return

    data = input("Data do agendamento (dd/mm/yyyy): ")
    forma_pagamento = input("Forma de pagamento (cartão/dinheiro/pix): ")

    cliente.agendar_procedimento(data, procedimento.nome, forma_pagamento)
    orientacoes = input("Orientações pós-procedimento: ")
    cliente.definir_orientacoes(orientacoes)

# Execução principal
if __name__ == '__main__':
    dados = carregar_dados()
    clientes = {c['cpf']: Cliente(**c) for c in dados.get('clientes', [])}
    admin = Administrador('Admin', '123456789', 30)
   
    while True:
        menu()
        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            cliente = cadastro_cliente()
            clientes[cliente.cpf] = cliente  # Armazenando cliente no dicionário pelo CPF
            salvar_dados({"clientes": [vars(c) for c in clientes.values()]})

        elif opcao == '2':
            agendar_cliente(clientes)
            salvar_dados({"clientes": [vars(c) for c in clientes.values()]})

        elif opcao == '3':
            cpf_cliente = input("Digite o CPF do cliente: ")
            if cpf_cliente in clientes:
                admin.cancelar_agendamento(clientes[cpf_cliente])
                salvar_dados({"clientes": [vars(c) for c in clientes.values()]})
            else:
                print("Cliente não encontrado.")

        elif opcao == '4':
            cpf_cliente = input("Digite o CPF do cliente: ")
            if cpf_cliente in clientes:
                admin.historico_tratamentos(clientes[cpf_cliente])
            else:
                print("Cliente não encontrado.")

        elif opcao == '5':
            cpf_cliente = input("Digite o CPF do cliente: ")
            if cpf_cliente in clientes:
                admin.faturamento(clientes[cpf_cliente])
            else:
                print("Cliente não encontrado.")
        
        elif opcao == '6':
            cpf_cliente = input("Digite o CPF do cliente:")
            if cpf_cliente in clientes:
                admin.editar_agendamento(clientes[cpf_cliente])
                salvar_dados({"clientes": [vars (c) for c in clientes.values()]}) #cria uma lista de dicionario com dados de todos os clientes, e salva no json
            else:
                print("Cliente não encontrado")

        elif opcao == '7':
            admin.sortear_cliente_premiado(clientes)
            print("sorteio realizado")
    

        elif opcao == '8':
            print("\nEncerrando o sistema. Até logo!")
            break

        else:
            print("Opção inválida!")