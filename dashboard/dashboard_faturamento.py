import pandas as pd 
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
dados = st.file_uploader("faturamento")
if dados:
    df = pd.read_csv(dados, sep=";")
    df['total'] = df['qtd'] * df['preco']
    df['mes'] = df['data'].apply(lambda x: int(x.split("/")[1]))

    lojas = df['loja'].unique()
    loja_selec = st.selectbox("loja", options=lojas)
    
    df_loja = df.query(f"loja == '{loja_selec}'")

    df_dinamica = pd.pivot_table(df_loja, index="mes", columns='produto', aggfunc="sum", values="total")

    col1, col2 = st.columns(2)
    with col1:
        df_dinamica

    with col2:
        df_dinamica.plot(kind="bar")
        plt.title(f'Faturamento por produto da loja {loja_selec}')
        plt.xlabel('meses')
        plt.ylabel('faturamento')
        st.pyplot(plt.gcf())
