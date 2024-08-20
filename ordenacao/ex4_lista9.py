def subir(lista):
    pos = len(lista) - 1
    while pos > 0:
        if lista[pos] < lista[pos-1]:
            aux = lista[pos]
            lista[pos] = lista[pos-1]
            lista[pos-1] = aux
        pos = pos - 1

def bubble_sort(lista):
    for i in range(len(lista)):
        subir(lista)

if __name__ == "__main__":
    lst = ['Ana', 'Adriana', 'Alex', 'Andre', 'Audrey', 'Alana', 'Artur']
    bubble_sort(lst)
    print(lst)        