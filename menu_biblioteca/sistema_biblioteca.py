import os

os.system('cls')
opcao = 123537
while opcao != 6:
    print("Bem-vindo à Biblioteca FIAP")
    print("1 - Reserva Livro\n2 - Cadastra Livro")
    print("3 - Devolução\n4 - Consulta Livro")
    print("5 - Cadastro do Leitor\n6 - Sair")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        isbn = input("Informe o isbn do livro: ")
        leitor = input("CPF do leitor: ")
        print("disponível a partir do dia: 25/04/2024")
        confirmacao = input("Deseja reservar (s/n): ")
    elif opcao == 2:
        pass
    elif opcao == 3:
        pass
    elif opcao == 4:
        pass
    elif opcao == 5:
        nome = input("Informe o nome: ")
        cpf = input("Informe o CPF: ")
        celular = input("Celular: ")
        rm = int(input("RM: "))
        print("Cadastro efetuado com sucesso!")
    elif opcao == 6:
        print("Até logo!")
    else:
        print("Opção Inválida!\n")
