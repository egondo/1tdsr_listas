#Inserindo registro

import oracledb

conn = oracledb.connect(user="pf0313", password="professor#23",
                      dsn="oracle.fiap.com.br/orcl")
cur = conn.cursor()
ins = '''insert into medico(nome, especialidade) 
                values(:nome, :especialidade)'''

cur.execute(ins, {"nome": "Adib Jatene", 
                    "especialidade": "cardiologista"})

conn.commit()
cur.close()
conn.close()