import oracledb

def get_conexao():
    return oracledb.connect(user="pf0313", password="professor#23",
                            dsn="oracle.fiap.com.br/orcl")

def converte(registro):
    return {'id': registro[0], 'modelo': registro[1], 
            'montadora': registro[2], 'placa': registro[3],
            'ano': registro[4]}

def consulta_todos():
    sql = "select id, modelo, montadora, placa, ano from tb_carro"
    lista = []
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql)
            dados = cur.fetchall()
            for reg in dados:
                lista.append(converte(reg))
    return lista

def consulta_id(id):
    sql = "select id, modelo, montadora, placa, ano from tb_carro where id=:id"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, {"id": id})
            dado = cur.fetchone()
            if dado:
                return converte(dado)
            else:
                return None

def insere(carro):
    sql = "insert into tb_carro(modelo, montadora, placa, ano) values(:modelo, :montadora, :placa, :ano) returning id into :id"
    
    with get_conexao() as con:
        with con.cursor() as cur:
            novo_id = cur.var(oracledb.NUMBER)
            carro['id'] = novo_id
            cur.execute(sql, carro)
        con.commit()
        carro['id'] = novo_id.getvalue()[0] 

def altera(carro):
    sql = "update tb_carro set modelo=:modelo, montadora=:montadora, placa=:placa, ano=:ano where id=:id"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, carro)
        con.commit()

if __name__ == "__main__":
    c = {"modelo": "FIT", "montadora": "Honda", "ano": 2015, "placa": "TRE-2830"}

    insere(c)        