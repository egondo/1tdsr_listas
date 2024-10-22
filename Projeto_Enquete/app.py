import negocio

enquete = negocio.recupera_enquete(4)
print(enquete['nome'], enquete['categoria'])
respostas = []
for questao in enquete['perguntas']:
    print(f"{questao['numero']}) {questao['texto']}")
    tipo = questao['tipo']
    if tipo == 2 or tipo == 3:
        for opcao in questao['opcoes']:
            print(f"{opcao['rotulo']} - {opcao['alternativa']}")
    resp = input("Resp: ")
    r = {"texto": resp, "id_pergunta": questao['id']}
    respostas.append(r)

pes = {"nome": "Joao Pedro", "idade": 23, "escolaridade": "superior", "municipio": "São Paulo", "sexo": "masculino"}
negocio.cadastra_respostas(pes, respostas)
