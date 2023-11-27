resp = 1

'''Colocar funcionalidades iguais as de Java'''

suporte_comunitario_info = [
    "Suporte Comunitário",
    "O suporte Comunitário é um local onde o usuário poderá compartilhar experiências, fazer perguntas e oferecer apoio uns aos outros.",
]
diario_saude_info = [
    "Diário de Saúde Personalizado",
    "Diário de Saúde Personalizado é uma funcionalidade que permite que usuários mantenham um diário de saúde pessoal, onde eles possam registrar sintomas, emoções, atividades físicas e outros detalhes relevantes para o seu bem-estar.",
]
registro_menstrual_info = [
    "Registro Menstrual",
    "A funcionalidade de Registro Menstrual permite que usuários rastreiem seu ciclo menstrual, sintomas associados e humor.",
]
integracao_dispositivos_info = [
    "Integração de Dispositivos de Saúde",
    "A funcionalidade de Integração de Dispositivos de Saúde permite que os usuários façam a integração de dispositivos de saúde, como smartwatches e monitores de pressão arterial, para coletar dados de saúde em tempo real.",
]
acompanhamento_transicao_info = [
    "Acompanhamento da Transição de Gênero",
    "A funcionalidade de Acompanhamento da Transição de Gênero permite que usuários registrem e acompanhem marcos na transição de gênero, como hormonioterapia, cirurgias e consultas médicas especializadas.",
]

while resp != 0:
    print("1 - Suporte Comunitário")
    print("2 - Diário de Saúde Personalizado")
    print("3 - Registro Menstrual")
    print("4 - Integração de Dispositivos de Saúde")
    print("5 - Acompanhamento da Transição de Gênero")

    opc = int(input("Digite a opção desejada: "))

    match opc:
        case 1:
            print(suporte_comunitario_info[1])
        case 2:
            print(diario_saude_info[1])
        case 3:
            print(registro_menstrual_info[1])
        case 4:
            print(integracao_dispositivos_info[1])
        case 5:
            print(acompanhamento_transicao_info[1])
        case _:
            print("Opção inválida")

    resp = int(input("Você deseja realizar uma nova operação (1-Sim / 0-Não)? "))
