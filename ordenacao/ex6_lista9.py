def organiza(lista, pos, criterio):
    aux = lista[pos]

    while pos > 0 and lista[pos-1][criterio] > aux[criterio]:
        lista[pos] = lista[pos-1]
        pos = pos - 1

    lista[pos] = aux
 
def insertion_sort(lista, criterio):
    for i in range(1, len(lista)):
        organiza(lista, i, criterio)


pessoas = [('Andre', 18), ('Thiago', 23), ('Soraia', 22), ('Mateus', 16), ('Bernardo', 23), ('Cibele', 17), ('Oscar', 18), ('Thiago', 15), ('Cintia', 16), ('Daniela', 15), ('Mario', 18), ('Soraia', 16), ('Lais', 16), ('Cintia', 20), ('Mario', 22)]
insertion_sort(pessoas, 1)
insertion_sort(pessoas, 0)
print(pessoas)


