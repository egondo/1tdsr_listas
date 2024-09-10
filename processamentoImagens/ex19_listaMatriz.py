import Imagem

def addRetangulo(matriz: list, pos: int, altura: int):
    colIni = pos
    colFinal = colIni + 49
    linFinal = 550
    linIni = linFinal - altura * 5

    while linIni < linFinal:
        colIni = pos
        while colIni < colFinal:
            matriz[linIni][colIni] = 0
            colIni = colIni + 1
        linIni = linIni + 1
    
    

imagem = []
for _ in range(600):
    imagem.append([255] * 800)

addRetangulo(imagem, 50, 80)
addRetangulo(imagem, 100, 65)
addRetangulo(imagem, 150, 87)
addRetangulo(imagem, 200, 74)

Imagem.salvaImagemCinza("histograma.png", imagem)
    