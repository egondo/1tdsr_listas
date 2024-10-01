import banco

def cria_time(nome: str) -> dict:
    time = banco.recupera_nome(nome)
    if time == None:
        time = {'nome': nome, 'vitorias': 0, 
                'empates': 0, 'derrotas': 0, 'gols_contra': 0,
                'gols_pro': 0}
        banco.insere_time(time)
    return time
    

#{'casa': 'Botafogo', 'gc':3, 'visi': 'Santos', 'gv': 2}
def cadastra_partida(partida: dict):
    time_casa = cria_time(partida['casa'])
    time_visi = cria_time(partida['visi'])
    
    if partida['gc'] > partida['gv']:
        time_casa['vitorias'] = time_casa['vitorias'] + 1
        time_visi['derrotas'] = time_visi['derrotas'] + 1
    elif partida['gc'] < partida['gv']:
        time_casa['derrotas'] = time_casa['derrotas'] + 1
        time_visi['vitorias'] = time_visi['vitorias'] + 1
    else:
        time_casa['empates'] = time_casa['empates'] + 1
        time_visi['empates'] = time_visi['empates'] + 1
    
    time_casa['gols_pro'] = time_casa['gols_pro'] + partida['gc']
    time_casa['gols_contra'] = time_casa['gols_contra'] + partida['gv']

    time_visi['gols_pro'] = time_visi['gols_pro'] + partida['gv']
    time_visi['gols_contra'] = time_visi['gols_contra'] + partida['gc']

    banco.atualiza_time(time_casa)
    banco.atualiza_time(time_visi)

    partida['casa'] = time_casa['id']
    partida['visi'] = time_visi['id']
    banco.insere_partida(partida)


def monta_tabela_classificacao():
    #dados = banco.recupera_times()
    #processar a lista dados gerando as outras informações e 
    # imprimir a tabela na tela.    
    dados = banco.recupera_times_completo()
    for reg in dados:
        print(reg)