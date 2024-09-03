def grava_pecas(matriz):
    #vamos usar o separador ; (semicolon)
    arq = open("pecas.csv", mode="w")
    for peca in matriz:
        for info in peca:
            arq.write(str(info))
            arq.write(";")
        arq.write("\n")
    arq.close()

def le_pecas(nome: str) -> list:
    arq = open(nome, mode='r')
    resultado = []
    for linha in arq:
        campos = linha.split(";")
        reg = [campos[0], campos[1], campos[2], float(campos[3]), int(campos[4])]
        resultado.append(reg)
    
    return resultado
