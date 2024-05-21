def intersecta(listaA: list, listaB: list):
    listaC = []
    for elem in listaA:
        if elem in listaB:
            listaC.append(elem)
    return listaC

conj_a = [1, 5, 9, 7, 3, 2, -10]
conj_b = [-1, 0, 6, 9, 2, 5]

resultado = intersecta(conj_a, conj_b)
print(resultado)

