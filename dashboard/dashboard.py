import pandas as pd 
import matplotlib.pyplot as plt

df_fatura = pd.read_csv("faturamento.txt", sep=';')
df_fatura['total'] = df_fatura['qtd'] * df_fatura['preco']

df_fatura['mes'] = df_fatura['data'].apply(lambda x: int(x.split('/')[1]))

#print(df_fatura.head(10))

df_tabela_dinamica = pd.pivot_table(df_fatura, index=['mes'], columns=['loja'], aggfunc="sum", values="total")

print(df_tabela_dinamica)

df_tabela_dinamica.plot(kind="bar")
plt.title('Faturamento mensal das lojas')
plt.xlabel('mes')
plt.ylabel('total')
plt.xticks(rotation=0)

plt.show()

df_celular = df_fatura.query("produto == 'celular'")
print(df_celular)

