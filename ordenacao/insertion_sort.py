def organiza(lista, pos):
    aux = lista[pos]
    while pos > 0 and lista[pos-1] > aux:
        lista[pos] = lista[pos-1]
        pos = pos - 1

    lista[pos] = aux

def insertion_sort(lista):
    for i in range(1, len(lista)):
        organiza(lista, i)


if __name__ == "__main__":
    lst = [-3, 7, 2, 18, 5, 0, 1, 5, 3, 6, 11]
    insertion_sort(lst)
    print(lst)
