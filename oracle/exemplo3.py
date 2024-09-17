import oracledb

conn = oracledb.connect(user="pf0313", password="professor#23",
                        dsn="oracle.fiap.com.br/orcl")

cursor = conn.cursor()
upt = "update medico set crm=:crm where id=:id"
medico = {"crm": '192922', "id": 22}

cursor.execute(upt, medico)
conn.commit()
cursor.close()
conn.close()