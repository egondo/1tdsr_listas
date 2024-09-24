import oracledb

def get_conexao():
    return oracledb.connect(user="pf0313", password="professor#23",
                            dsn="oracle.fiap.com.br/orcl")

def insere_filme(movie: dict):
    sql = '''INSERT into tb_filme(titulo, diretor, atores, nota,
    data_lancamento, sinopse, estudio) values(:titulo, :diretor,
    :atores, :nota, to_date(:data_lancamento, 'DD-MM-YYYY'),
    :sinopse, :estudio)'''

    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, movie)
        conn.commit()


def consulta_filme(ator: str) -> list:
    sql = '''select id, titulo, diretor, atores, 
        data_lancamento, nota, estudio, sinopse from tb_filme
        where atores like :atores'''
    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, {"atores": f"%{ator}%"}) 
            lista = cur.fetchall()
            return lista
               
def apaga_filme(id: int):
    sql = "delete from tb_filme where id = :id"
    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, {"id": id})
        conn.commit()

def atualiza_filme(movie: dict):
    sql = '''update tb_filme set titulo=:titulo, sinopse=:sinopse,
            nota=:nota, diretor=:diretor, atores=:atores, 
            estudio=:estudio, 
            data_lancamento=to_date(:data, 'DD-MM-YYYY')
            where id=:id'''
    
    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, movie)
        conn.commit()
