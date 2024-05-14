import baralho as bar

def imprime(mao: list):
    s = ""
    for carta in mao:
        s = s + bar.to_str(carta)
    return s

deck = bar.cria()
bar.embaralha(deck)

jog_A = bar.distribui(deck, 2)
jog_B = bar.distribui(deck, 2)
mesa = bar.distribui(deck, 5)

print("Jogador A ", imprime(jog_A))
print("Mesa: ", imprime(mesa))
print("Jogador B ", imprime(jog_B))