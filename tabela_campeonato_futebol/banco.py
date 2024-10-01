import oracledb

def get_conexao():
    return oracledb.connect(user='pf0313', password='professor#23',
                            dsn='oracle.fiap.com.br/orcl')

#{'casa': 3, 'gc': 2, 'visi': 5, 'gv': 2, 'rodada': 1}
def insere_partida(partida: dict):
    sql = '''insert into tb_partida(rodada, gols_casa, gols_visitante, 
            id_casa, id_visitante) values(:rodada, :gc, 
            :gv, :casa, :visi)'''
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, partida)
        con.commit()

#{'nome': nome, 'vitorias': 0, 'empates': 0, 'derrotas': 0, 'gols_contra': 0,'gols_pro': 0, 'id': 10}
def atualiza_time(time: dict):
    sql = '''update tb_time set nome=:nome, vitorias=:vitorias, empates=:empates, derrotas=:derrotas, gols_contra=:gols_contra, gols_pro=:gols_pro where id=:id'''
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, time)
        con.commit()

def recupera_nome(nome: str) -> dict:
    sql = '''select id, nome, vitorias, empates, derrotas, gols_pro, gols_contra from tb_time where nome=:nome'''
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, {'nome': nome})
            reg = cur.fetchone()
            if reg:
                return {'id': reg[0], 'nome': reg[1], 'vitorias': reg[2], 'empates': reg[3], 'derrotas': reg[4], 'gols_pro': reg[5], 'gols_contra': reg[6]}
            else:
                return None
            

#{'nome': nome, 'vitorias': 0, 'empates': 0, 'derrotas': 0, 'gols_contra': 0,'gols_pro': 0}            
def insere_time(time: dict):
    sql = '''insert into tb_time(nome, vitorias, empates, derrotas, gols_contra, gols_pro) values(:nome, :vitorias, :empates, :derrotas, :gols_contra, :gols_pro) returning id into :id'''
    with get_conexao() as con:
        with con.cursor() as cur:
            new_id = cur.var(oracledb.NUMBER)
            time['id'] = new_id
            cur.execute(sql, time)
            time['id'] = new_id.getvalue()[0]
        con.commit()


def recupera_times_completo():
    sql = '''select nome, vitorias * 3 + empates as pg, vitorias + empates + derrotas as jogos, vitorias, empates, derrotas, gols_contra, gols_pro, gols_pro - gols_contra as saldo, (vitorias*3 + empates) / ((vitorias+empates+derrotas) * 3) from tb_time order by pg desc'''
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql)
            return cur.fetchall()