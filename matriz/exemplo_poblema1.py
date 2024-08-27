def imprime(matriz):
    for linha in matriz:
        print(linha)

if __name__ == "__main__":
    mat = []
    i = 0
    while i < 4:
        mat.append([0] * 5)
        i = i + 1
        
    num = 1
    i = 0
    while i < 4:
        j = 0
        while j < 5:
            mat[i][j] = num
            j = j + 1
            num = num + 1
        i = i + 1

    imprime(mat)    