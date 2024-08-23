matriz = []
for i in range(4):
    matriz.append([0] * 5)

num = 1
for lin in range(4):
    for col in range(5):
        matriz[lin][col] = num
        num = num + 1

for linha in matriz:
    print(linha)
