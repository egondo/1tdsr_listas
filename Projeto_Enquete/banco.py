import oracledb
import os

def get_conexao():
    #usuario = os.getenv("USER_ORA")
    #senha = os.getenv("PWD_ORA")
    return oracledb.connect(user="pf0313", password="professor#23", 
    dsn="oracle.fiap.com.br/orcl")


def insere_enquete(enq: dict):
    sql = "insert into tbr_enquete(nome, categoria) values(:nome, :categoria) returning id into :id"
    dado = {"nome": enq['nome'], "categoria": enq['categoria']}
    with get_conexao() as con:
        with con.cursor() as cur:
            novo_id = cur.var(oracledb.NUMBER)
            dado['id'] = novo_id
            cur.execute(sql, dado)
            enq['id'] = novo_id.getvalue()[0]
        con.commit()

def insere_pergunta(perg: dict):
    sql = "insert into tbr_pergunta(texto, tipo, numero,id_enquete) values(:texto, :tipo, :numero, :id_enquete) returning id into :id"
    with get_conexao() as con:
        with con.cursor() as cur:
            novo_id = cur.var(oracledb.NUMBER)
            perg['id'] = novo_id
            cur.execute(sql, perg)
            perg['id'] = novo_id.getvalue()[0]
        con.commit()        

def insere_opcao(opcao: dict):
    sql = "insert into tbr_opcoes(alternativa, rotulo, id_pergunta) values(:alternativa, :rotulo, :id_pergunta)"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, opcao)
        con.commit()








