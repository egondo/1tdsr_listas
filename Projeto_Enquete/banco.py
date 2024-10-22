import oracledb
import os

def get_conexao():
    #usuario = os.getenv("USER_ORA")
    #senha = os.getenv("PWD_ORA")
    return oracledb.connect(user="pf0313", password="professor#23", 
    dsn="oracle.fiap.com.br/orcl")

def insere_pessoa(pes: dict):
    sql = "insert into tbr_pessoa(nome, idade, sexo, municipio, escolaridade) values(:nome, :idade, :sexo, :municipio, :escolaridade) returning id into :id"
    con = get_conexao()
    cur = con.cursor()
    novo_id = cur.var(oracledb.NUMBER)
    pes['id'] = novo_id
    cur.execute(sql, pes)
    con.commit()
    pes['id'] = novo_id.getvalue()[0]
    cur.close()
    con.close()

def insere_resposta(resp: dict):
    sql = "insert into tbr_resposta(texto, datahora, id_pessoa, id_pergunta) values(:texto, current_timestamp, :id_pessoa, :id_pergunta)"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, resp)
        con.commit()


def recupera_enquete(id: int) -> dict:
    sql = "select id, nome, categoria from tbr_enquete where id = :id"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, {"id": id})
            dado = cur.fetchone()
    return {"id": dado[0], "nome": dado[1], "categoria": dado[2]}

def recupera_perguntas_enquete(id_enquete: int) -> list:
    sql = "select p.id, p.texto, p.tipo, p.numero, o.alternativa, o.rotulo from tbr_pergunta p left join tbr_opcoes o on p.id=o.id_pergunta where p.id_enquete = :id order by p.numero, o.rotulo"
    
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, {"id": id_enquete})
            registros = cur.fetchall()
    lista = []
    aux_id = 0
    pergunta = {}
    for reg in registros:
        if aux_id != reg[0]:
            pergunta = {"id": reg[0], "texto": reg[1], "tipo": reg[2], "numero": reg[3]}
            aux_id = reg[0]
            lista.append(pergunta)

        if reg[2] == 2 or reg[2] == 3:
            opcao = {"alternativa": reg[4], "rotulo": reg[5]}
            if not "opcoes" in pergunta:
                pergunta['opcoes'] = []
            pergunta['opcoes'].append(opcao)
    
    return lista

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








