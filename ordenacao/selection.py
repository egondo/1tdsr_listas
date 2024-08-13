def menor(lista: list, pos: int):
    ind = pos
    while pos < len(lista):
        if lista[pos] < lista[ind]:
            ind = pos
        pos = pos + 1
    return ind

def selection_sort(lista: list):
    i = 0
    while i < len(lista):
        pos = menor(lista, i)
        aux = lista[pos]
        lista[pos] = lista[i]
        lista[i] = aux
        i = i + 1

lst = [3, 4, 9, 0, 8]
selection_sort(lst)
print(lst)    