import Imagem

def tem_vizinho_branco(matriz, i, j):
    if matriz[i][j] == 255:
        return True
    if i - 1 >= 0 and j-1 >= 0 and matriz[i-1][j-1] == 255:
        return True
    if i - 1 >= 0 and matriz[i-1][j] == 255:
        return True
    if i - 1 >= 0 and j + 1 < len(matriz[i]) and matriz[i-1][j+1] == 255:
        return True
    if j - 1 >= 0 and matriz[i][j-1] == 255:
        return True
    if j + 1 < len(matriz[i]) and matriz[i][j+1] == 255:
        return True
    
    if i + 1 < len(matriz) and j-1 >= 0 and matriz[i+1][j-1] == 255:
        return True
    if i + 1 < len(matriz) and matriz[i+1][j] == 255:
        return True
    if i + 1 < len(matriz) and j + 1 < len(matriz[i]) and matriz[i+1][j+1] == 255:
        return True
    
    return False


matriz = Imagem.getMatrizImagemCinza("yao-ming.png")
lin = len(matriz)
col = len(matriz[0])
mat2 = []
for i in range(lin):
    mat2.append([0] * col)
for i in range(lin):
    for j in range(col):
        if tem_vizinho_branco(matriz, i, j):
            mat2[i][j] = 255
Imagem.salvaImagemCinza("yao-ming1.png", mat2)
