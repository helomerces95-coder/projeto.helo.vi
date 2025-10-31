import json

def menu ():
    while True:
        print("SEJA BEM-VINDO A CLÍNICA DE PROCEDIMENTOS ESTETICOS JK")
        print("Escolha uma das opções a seguir:\n")
        opcao = input("""
                    1 - Cadastro de Cliente
                    2 - Agendar procedimento
                    3 - Cancelar agendamento
                    4 - Histórico de tramento
                    5 - Faturamento
                    6 - sair  
                      """)
        
        if opcao == '1':
            def cadastro_cliente ():
                nome = input("digite o seu nome:\n")
                cpf = input("digite o seu cpf:\n")
                idade = int(input("digite a sua idade:\n"))
                telefone = int(input("digite o seu número de telefone:\n"))
                
                cliente = Cliente(nome, cpf,idade,telefone)
                print(f"{nome}, foi cadastrado com sucesso!🤩")
                return cliente
            
        if opcao == '2':
            def agendar_procedimento ():
                print("Escolha uma das categorias para o agendamento do seu procedimento!")
                categoria = input("""
                                Procedimentos Faciais👩🏽‍🦲
                                  1 - limpeza de pele
                                  2 - botox 
                                  3 - tratamento para acne
                                Procedimentos Corporais 🦸🏽‍♀️
                                   4 - drenagem 
                                   5 - massagem modeladora
                                   6 - tratamento de estrias 
                                Procedimentos Capilares 👩🏽
                                   7 - tratamento para queda
                                   8 - hidratação capilar 
                                  """)
                print(f" O procedimento {categoria}, está agendado! ")
        if opcao == '3':
            agendamentos = {
                agendar_procedimento
            }
            def cancelar_procedimento (identificador):
                if identificador in agendamentos:
                    del agendamentos [identificador] #remove referências de nomes, variavel e afins
                    

                
                