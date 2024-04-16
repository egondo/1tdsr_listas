n = int(input("Informe n: "))

if n == 1 or n == 2:
    print(1)
else:
    ant = 1
    atual = 1
    contador = 2
    while contador < n:
        prox = atual + ant
        ant = atual
        atual = prox
        contador = contador + 1
    print(atual)


