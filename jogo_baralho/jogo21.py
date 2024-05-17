import baralho as bar

def jogada(mao):
    linha = ""
    for carta in mao:
        linha = f"{linha} {bar.to_str(carta)}"
    print(linha)
    print(f"Pontos: {soma_pontos(mao)}")
    resp = input("Deseja mais cartas (s/n)? ")
    return resp

def soma_pontos(mao):
    soma = 0
    for carta in mao:
        if carta[0] > 10:
            soma = soma + 10
        else:
            soma = soma + carta[0]
    return soma


def jogada_cpu(mao):
    if soma_pontos(mao) < 16:
        return True
    return False


deck = bar.cria()
bar.embaralha(deck)

mao_hum = bar.distribui(deck, 2)
mao_cpu = bar.distribui(deck, 2)

decisao = jogada(mao_hum)
while decisao == 's':
    carta = bar.compra(deck)
    mao_hum.append(carta)
    decisao = jogada(mao_hum)


decisao = jogada_cpu(mao_cpu)
while decisao == True:
    carta = bar.compra(deck)
    mao_cpu.append(carta)
    decisao = jogada_cpu(mao_cpu)

pontos_hum = soma_pontos(mao_hum)
pontos_cpu = soma_pontos(mao_cpu)
print(f"Jog: {pontos_hum} X CPU: {pontos_cpu}")

if pontos_cpu <= 21 and pontos_hum <= 21:
    if pontos_hum > pontos_cpu:
        print("Parabéns você ganhou!")
    else:
        print("Você perdeu!")
elif pontos_cpu <= 21 and pontos_hum > 21:
    print("Você perdeu!")
elif pontos_cpu > 21 and pontos_hum <= 21:
    print("Parabéns você ganhou!")
else:
    if pontos_hum < pontos_cpu:
        print("Parabéns você ganhou!")
    else:
        print("Você perdeu!")







