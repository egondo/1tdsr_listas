import time

def busca(conjunto: list, valor: object) -> int:
    i = 0
    while i < len(conjunto) and conjunto[i] != valor:
        i = i + 1

    if i == len(conjunto):
        return -1
    else:
        return i
    
def busca_for(conjunto: list, valor: object) -> int:
    for i in range(len(conjunto)):
        if conjunto[i] == valor:
            return i
    return -1    

def busca_binaria(conjunto: list, valor: object) -> int:
    ini = 0
    fim = len(conjunto) - 1
    while ini <= fim:
        meio = (ini + fim) // 2
        if conjunto[meio] < valor:
            ini = meio + 1
        elif conjunto[meio] > valor:
            fim = meio - 1
        else:
            return meio
    return -1


if __name__ == '__main__':
    lst = [0] * 400_000_000
    x = 10

    ini = time.time()
    resp = busca_binaria(lst, x)
    fim = time.time()
    print(fim - ini, "busca binaria")

    ini = time.time()
    resp = busca_for(lst, x)
    fim = time.time()
    print(fim - ini, "busca com for")
    #print(resp)

