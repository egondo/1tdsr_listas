def insere_ordenado(x, lista):
    i = 0
    while i < len(lista) and lista[i] < x:
        i = i + 1
    lista.insert(i, x)


vet = [1, 6, 10, 24, 25, 30, 45]
insere_ordenado(20, vet)
print(vet)