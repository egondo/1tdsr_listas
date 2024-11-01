import streamlit as st

st.set_page_config(layout="wide")
st.markdown("Hello World!")

(col1, col2) = st.columns(2)

with col1:
    nome = st.text_input("Nome: ")
    data = st.text_input("Data: ")
    papel = st.selectbox("Papel", options=["Professor", "Aluno"])

with col2:
    st.write(nome)
    st.write(data)
    st.markdown(papel)