def menor(lista: list, pos: int):
    ind = pos
    while pos < len(lista):
        if lista[pos] < lista[ind]:
            ind = pos
        pos = pos + 1
    return ind

l = [0, 7, 5, -2, 4, 6, -1, 0, 3]
print(menor(l, 0))

