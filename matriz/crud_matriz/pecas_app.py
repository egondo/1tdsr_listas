def insere_pecas(matriz: list):
    nome = input("Nome: ")
    serie = input("Série: ")
    origem = input("Origem: ")
    preco = float(input("Preço: "))
    qtd = int(input("Quantidade: "))
    registro = [nome, serie, origem, preco, qtd]
    matriz.append(registro)

def consulta_pecas(matriz: list):
    orig = input("Informe a origem: ")
    for i in range(len(matriz)):
        if matriz[i][2] == orig:
            print(matriz[i])

def busca(matriz: list, serie: str) -> int:
    for i in range(len(matriz)):
        if matriz[i][1] == serie:
            return i
    return -1

def exclui_pecas(matriz: list):
    serie = input("Série: ")
    pos = busca(matriz, serie)
    if pos == -1:
        print("Nenhuma peça encontrada")
    else:
        info = matriz.pop(pos)
        print(info)
        print("Foi excluída com sucesso!")

def altera_pecas(matriz: list):
    #deixar para vcs fazerem 10min




if __name__ == "__main__":
    opcao = 0
    estoque = []
    while opcao != 5:
        print("SISTEMA DE PEÇAS")
        print("1 - insere")
        print("2 - altera")
        print("3 - consulta")
        print("4 - exclui")
        print("5 - sai")
        opcao = int(input("Selecione uma opção: "))

        if opcao == 1:
            insere_pecas(estoque)
        elif opcao == 2:
            altera_pecas(estoque)
        elif opcao == 3:
            consulta_pecas(estoque)
        elif opcao == 4:
            exclui_pecas(estoque)