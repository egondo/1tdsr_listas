import random

def cria_vetor(qtd):
    lst = []
    for x in range(qtd):
        lst.append(random.randint(1, 1000))
    return lst


lista = cria_vetor(100)
print (lista)