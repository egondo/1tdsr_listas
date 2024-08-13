def busca(lista: list, valor, pos):
    while pos < len(lista) and lista[pos] != valor:
        pos = pos + 1

    if pos < len(lista):
        return pos
    else:
        return -1
    
lst = [2, 5, -7, 9, 3, 10, 15, 6]
x = 11
for i in range(len(lst)):
    valor = x - lst[i]
    resp = busca(lst, valor, i + 1)
    if resp != -1:
        print(lst[i], lst[resp])
        
