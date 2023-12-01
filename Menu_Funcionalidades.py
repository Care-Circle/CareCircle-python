Ciclo_menstrual = ["Ciclo Menstrual, aqui o usuário poderá acompanhar e registrar seu ciclo menstrual de forma prática e intuitiva, recebendo lembretes personalizados para ajudar a monitorar sua saúde reprodutiva."]
grupo_apoio = ["Grupo de apoio, o grupo de apoio serve para se conectar com uma comunidade solidária e compartilhar experiências, obter orientações e encontrar apoio emocional durante diferentes fases da vida."]
hospitais_proximos = ["Hospitais mais proximos, Aqui o usuário consiguirá  Localizar facilmente hospitais próximos à sua localização, obtenha informações sobre serviços oferecidos e planeje cuidados médicos com mais eficiência."]
marcas_parceiras = ["Marcas parceiras, aqui o usupario poderá explorar ofertas exclusivas de marcas parceiras, proporcionando aos usuários benefícios especiais relacionados à saúde feminina e a comunidade lgbtqia+. "]
login = ["Aqui é onde o usuário poderá ter acesso a sua conta com um login seguro, desfrutando de uma experiência personalizada"]
logoff = ["Aqui o usuário poderá fazer logoff de maneira simples para garantir a privacidade de suas informações."]
listar_grupo = ["Aqui o usuário terá uma lista de todos os grupos de apoio que faz parte"]
participar_grupo = ["Aqui o usuário terá a opção de participar de um grupo de apoio"]

publicacao = ["Permite que o administrador faça alguma publicação"]
Inserir_grupo = ["Essa funcionalidade permite que o administrador insira mais grupos de apoio na plataforma"]
Registrar_marca = ["Essa funcionalidade permite que o administrador registre novas marcas parceiras"]
logoff_adm = ["Aqui o administrado pode sair da sua pagina"]
listar_user = ["Essa funcionalidade permite ao administrador listar todos os usuários cadastrados"]
listar_marca = ["Essa funcionalidade permite ao administrador listar todas as marcas parceiras "]
listar_grupo = ["Essa funcionalidade permite ao administrador listar todos os grupos de apoio "]
listar_postagens = ["Essa funcionalidade permite ao administrador listar todas as postagens feitas" ]
listar_contas_adm = ["Essa funcionalidade permite ao administrador listar todas as contas administrativas existentes"]
listar_todas_contas = ["Essa funcionalidade permite ao administrador listar as contas de usuários e administrativas"]


while True:
    escolha_menu = int(input("Escolha o menu: 1 - Usuário, 2 - Administrador, 0 - Sair: "))

    if escolha_menu == 0:
        print("Você está saindo do programa. Até logo!")
        break
    elif escolha_menu == 1:
        resp = 1
        while resp != 0:
            print("-------- MENU USUÁRIO ---------")
            print("1 - Login")
            print("2 -  Adicionar um ciclo menstrual")
            print("3 - Grupos de apoio")
            print("4 - Participar de um grupo de apoio")
            print("5 - Listar grupos de apoio que faço parte")
            print("6 - Hospitais mais proximos")
            print("7 - Marcas parceiras")
            print("8 - Logoff")

            opc = int(input("Digite a opção desejada: "))

            match opc:
                case 1:
                    print(login[0])
                case 2:
                    print(Ciclo_menstrual[0])
                case 3:
                    print(grupo_apoio[0])
                case 4:
                    print(participar_grupo[0])
                case 5:
                    print(listar_grupo[0])
                case 6:
                    print(hospitais_proximos[0])
                case 7:
                    print(marcas_parceiras[0])
                case 8:
                    print(logoff[0])
                case _:
                    print("Opção inválida")

            resp = int(input("Você deseja realizar uma nova operação (1-Sim / 0-Não)? "))
            if resp == 0:
                print("Você está deixando o menu do usuário.")

    elif escolha_menu == 2:
        while True:
            print("-------- MENU ADMINISTRADOR ---------")
            print("1 - Realizar uma publicação")
            print("2 - Inserir um novo grupo de apoio")
            print("3 - Registrar nova marca parceira")
            print("4 - Listar todos os usuários")
            print("5 - Listar todas as marcas parceiras")
            print("6 - Listar todos os grupos de apoio")
            print("7 - Listar todas as postagens")
            print("8 - Listar todas as contas administrativas")
            print("9 - Listar todas as contas")
            print("10 - Logoff")

            adm = int(input("Digite o que deseja fazer de acordo com as opções: "))



            match adm:
                case 1:
                    print(publicacao[0])
                case 2:
                    print(Inserir_grupo[0])
                case 3:
                    print(Registrar_marca[0])
                case 4:
                    print(listar_user[0])
                case 5:
                    print(listar_marca[0])
                case 6:
                    print(listar_grupo[0])
                case 7:
                    print(listar_postagens[0])
                case 8:
                    print(listar_contas_adm[0])
                case 9:
                    print(listar_todas_contas[0])
                case 10:
                    print(logoff_adm[0])
                case _:
                    print("Opção inválida")
            admm = int(input("Você deseja realizar uma nova operação (1-Sim / 0-Não)? "))
            if admm == 0:
                print("Você está deixando o menu do administrador.")
                break

    else:
        print("Opção inválida. Por favor, escolha novamente.")
