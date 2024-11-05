import negocio
import streamlit as st

def busca(enquetes: list, nome) -> dict:
    for enq in enquetes:
        if enq['nome'] == nome:
            return enq
    return None

st.markdown("Página para responder a enquete")

#with st.form("form"):
nome = st.text_input("nome")
idade = st.text_input("idade")
escolaridade = st.selectbox("escolaridade", options=["", "fundamental", "médio", "superior", "pós-graduado"])
cidade = st.text_input("cidade")
genero = st.radio("gênero", options=["masculino", "feminino"])
    
lista_enquetes = negocio.recupera_todas_enquetes()
lista = [""]
for enq in lista_enquetes:
    lista.append(f"{enq['nome']}")

enq_selected = st.selectbox("enquete", options=lista)
   
if enq_selected != "":
    enquete_dict = busca(lista_enquetes, enq_selected)
    
    respostas = []
    for questao in enquete_dict['perguntas']:
        st.write(f"{questao['numero']}) {questao['texto']}")
        tipo = questao['tipo']
        if tipo == 2:
            lista = []
            for opcao in questao['opcoes']:
                lista.append(opcao['alternativa'])
            resp = st.radio('opçoes', options=lista, index=None)
        elif tipo == 3:
            aux = [''] * len(questao['opcoes'])
            i = 0
            for opcao in questao['opcoes']:
                aux[i] = st.checkbox(opcao['alternativa'])
                i = i + 1
            i = 0
            resp = ""
            while i < len(aux):
                if aux[i]:
                    resp = resp + questao['opcoes'][i]['alternativa'] + "; "
                i = i + 1            
        else:
            resp = st.text_input("Resp: ")
        r = {"texto": resp, "id_pergunta": questao['id']}
        respostas.append(r)

    botao = st.button("envia")
    if botao:
        st.write(respostas)
        pes = {"nome": nome, "idade": int(idade), "escolaridade": escolaridade, "municipio": cidade, "sexo": genero}
        st.write(pes)
        negocio.cadastra_respostas(pes, respostas)

