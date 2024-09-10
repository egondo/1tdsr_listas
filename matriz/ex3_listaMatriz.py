#Escreva um programa que declara uma matriz 5x7 de números inteiros e preenche todos os valores com números aleatórios no intervalo de 0 a 1000.

import random

matriz = []
for i in range(5):
    matriz.append([0] * 7)

for i in range(5):
    for j in range(7):
        matriz[i][j] = random.randint(0, 1000)

for lin in matriz:
    print(lin)    



