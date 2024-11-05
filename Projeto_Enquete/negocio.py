import banco

def recupera_enquete(id: int) -> dict:
    enquete = banco.recupera_enquete(id)
    perguntas = banco.recupera_perguntas_enquete(id)
    enquete['perguntas'] = perguntas
    return enquete

def recupera_todas_enquetes() -> list:
    ids = [4, 41, 5]
    lista = []
    for id in ids:
        enq = recupera_enquete(id)
        lista.append(enq)
    return lista

def cadastra_respostas(pes: dict, respostas: list):
    #pes = {"nome": "Joao Pedro", "idade": 23, "escolaridade": "superior",
    #       "municipio": "São Paulo"}
    banco.insere_pessoa(pes)

    for resp in respostas:
        resp['id_pessoa'] = pes['id']
        banco.insere_resposta(resp)


def cadastra_enquete(enq: dict):
    banco.insere_enquete(enq)
    id = enq['id']
    print("ID:", id)
    lista_perguntas = enq['perguntas']
    for perg in lista_perguntas:
        perg['id_enquete'] = id
        if perg['tipo'] == 2 or perg['tipo'] == 3:
            lista_opcoes = perg.pop('opcoes')

        banco.insere_pergunta(perg)
        if perg['tipo'] != 1:
            for opcao in lista_opcoes:
                opcao['id_pergunta'] = perg['id']
                banco.insere_opcao(opcao)

if __name__ == "__main__":

    info = {"nome":"Pesquisa de férias", 
            "categoria": "viagens",
            "perguntas":[
                {"texto": "Na sua última viagem para onde você foi?",
                "tipo": 1, "numero": 1
                },
                {"texto": "Como você chegou lá?",
                "tipo": 2, "numero": 2,
                "opcoes": [
                    {"alternativa": "Carro", "rotulo": 1},
                    {"alternativa": "Ônibus", "rotulo": 2},
                    {"alternativa": "Avião", "rotulo": 3},
                    {"alternativa": "Navio", "rotulo": 4}
                ]
                },
                {"texto": "Quais locais você gostaria de visitar?",
                 "tipo": 3, "numero": 3,
                 "opcoes": [
                     {"alternativa": "América", "rotulo": 1},
                     {"alternativa": "Ásia", "rotulo": 2},
                     {"alternativa": "África", "rotulo": 3},
                     {"alternativa": "Europa", "rotulo": 4},
                     {"alternativa": "Antártida", "rotulo": 5},
                 ]}
            ] 
            }
    cadastra_enquete(info)
