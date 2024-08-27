import Imagem

matriz = Imagem.getMatrizImagemCinza("/Users/eduardogondo/Downloads/1tdsr/1tdsr_listas/processamentoImagens/wallpaper.png")

for linha in matriz:
    print(linha)

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if matriz[i][j] > 128:
            matriz[i][j] = 255
        else:
            matriz[i][j] = matriz[i][j] - 20
            if matriz[i][j] < 0:
                matriz[i][j] = 0

Imagem.salvaImagemCinza("/Users/eduardogondo/wall.png", matriz)
print("Finalizado!")