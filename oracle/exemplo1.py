#abrir uma conexao com o banco
#abrir um cursor a partir da conexao
#com o cursor, podemos executar os comandos SQL
#fechamos o cursor 
#fechamos a conexao

import oracledb

url = "oracle.fiap.com.br/orcl"
conexao = oracledb.connect(user="pf0313", password="professor#23", 
                           dsn=url)
#print("Versao do banco", conexao.version)
cur = conexao.cursor()
cur.execute("select especialidade, nome from medico")
registros = cur.fetchall()
#que tipo de dado é o registros?
#registros é uma lista <class list

for reg in registros:
    print(reg)

cur.close()
conexao.close()