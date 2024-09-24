import banco

if __name__ == "__main__":
    filmes = banco.consulta_filme('Russel Crowe')
    for f in filmes:
        print(f)