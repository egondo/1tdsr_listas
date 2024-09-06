def cadastra_equipe(conferencia: dict):
    nome = input("Digite o nome: ")
    if nome in conferencia:
        print(f"ERRO, {nome} ja cadastrado")
    else:
        conferencia[nome] = []

def cadastra_jogador(conferencia: dict):
    time = input("Time: ")
    if not time in conferencia:
        print(f"ERRO, {time} não cadastrado")
    else:
        nome = input("Nome do jogador: ")
        camisa = int(input("Camisa: "))
        posicao = input("Posição: ")
        player = { "nome": nome, "numero": camisa,
            "posicao": posicao}

        conferencia[time].append(player)

def lista_equipe(conferencia: dict):
    time = input("Time: ")
    if not time in conferencia:
        print(f"{time} não existe!")
    else:
        for player in conferencia[time]:
            print(player.get('nome'), player.get('posicao'))


equipes = {}
opcao = 0
while opcao != 4:
    print("1 - Cadastra Equipe")
    print("2 - Cadastra Jogador")
    print("3 - Lista equipes")
    print("4 - Sair")
    opcao = int(input("Opcao: "))
    if opcao == 1:
        cadastra_equipe(equipes)
    elif opcao == 2:
        cadastra_jogador(equipes)
    elif opcao == 3:
        lista_equipe(equipes)
    