import exemplo_busca_simples as ebs

def elimina_repetidos(lista: list):

    resp = []
    #para cada valor da lista faço a busca e se o  
    #elemento nao esta na lista eu adiciono em resp
    #caso ele esteja na lista eu nao faco nada
    for valor in lista:
        if ebs.busca(resp, valor) == -1:
            resp.append(valor)
    return resp

lst = [2, 5, 6, 9, -1, 0, 7, 2, 4, 6, -1, 0]
r = elimina_repetidos(lst)
print(r)