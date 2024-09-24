import banco
import datetime

if __name__ == "__main__":
    tit = input("Titulo: ")
    dir = input("Diretor: ")
    dia_lanc = int(input("Dia do lançamento: "))
    mes_lanc = int(input("Mes do lançamento: "))
    ano_lanc = int(input("Ano do lançamento: "))
    data = datetime.datetime(ano_lanc, mes_lanc, dia_lanc)
    sin = input("Sinopse: ")
    nota = float(input("Nota: "))
    atores = input("Atores principais: ")
    estudio = input("Estúdio: ")

    #criando o dicionario que representa o filme
    movie = {}
    movie['titulo'] = tit
    movie['diretor'] = dir
    movie['data_lancamento'] = data
    movie['sinopse'] = sin
    movie['nota'] = nota
    movie['atores'] = atores
    movie['estudio'] = estudio

    banco.insere_filme(movie)