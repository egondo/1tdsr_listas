# Jogo entre 2 jogadores apenas que recebem 3 cartas iniciais
# Melhor 3 rodadas, aquele que vencer duas ganha a partida
# Se houver empate na primeira rodada, o vencedor é aquele que ganha
# a segunda rodada, caso persista empate, o vencedor é a aquele que ganha 
# a terceira rodada
# Cada jogador descarta uma carta em cada rodada e a vez de cada jogador
# depende da rodada anterior, por exemplo, se o jogador A ganhou a rodada
# anterio, ele deverá começar a próxima rodada.
# A ordem das cartas, da maior para a menor, é: 3, 2, A, K, J, Q, 7, 6, 5, 4 


#Agora, tente melhorar o jogo de truco acrescentand uma vira, ou seja, 
#as manilhas do jogo de truco

import baralho as bar
import random 

def jogada(mao):
    mao_txt = ""
    for c in mao:
        mao_txt = f"{mao_txt} {bar.to_str(c)}"
    print(mao_txt)
    sel = int(input("Informe a posicao da carta que deseja descartar: "))
    return mao.pop(sel)

def jogada_cpu(mao):
    pos = random.randint(0, len(mao) - 1)
    return mao.pop(pos)
    
def pontos(carta):
    if carta[0] >= 1 and carta[0] <= 3:
        return carta[0] * 30
    elif carta[0] == 11:
        return 12
    elif carta[0] == 12:
        return 11
    else:
        return carta[0]    

def ganhador(carta_um, carta_dois):
    print(bar.to_str(carta_um), bar.to_str(carta_dois))
    if pontos(carta_um) > pontos(carta_dois):
        return -1
    elif pontos(carta_um) == pontos(carta_dois):
        return 0
    else:
        return 1

deck = bar.cria('espanhol')
bar.embaralha(deck)

mao_jog = bar.distribui(deck, 3)
mao_cpu = bar.distribui(deck, 3)

ganho_jog = 0
ganho_cpu = 0
#Primeira rodada
carta_jog = jogada(mao_jog)
carta_cpu = jogada_cpu(mao_cpu)
resp = ganhador(carta_jog, carta_cpu)
if resp == -1:
    ganho_jog = ganho_jog + 1
elif resp == 1:
    ganho_cpu = ganho_cpu + 1
else:
    ganho_jog = ganho_jog + 1
    ganho_cpu = ganho_cpu + 1

#Segunda rodada
carta_jog = jogada(mao_jog)
carta_cpu = jogada_cpu(mao_cpu)
resp = ganhador(carta_jog, carta_cpu)
if resp == -1:
    ganho_jog = ganho_jog + 1
elif resp == 1:
    ganho_cpu = ganho_cpu + 1
else:
    ganho_jog = ganho_jog + 1
    ganho_cpu = ganho_cpu + 1

if ganho_jog == 2 and ganho_cpu < 2:
    print("Parabéns, você venceu!")
    exit()
elif ganho_cpu == 2 and ganho_jog < 2:
    print("A Cpu venceu")
    exit()

#terceira rodada
carta_jog = jogada(mao_jog)
carta_cpu = jogada_cpu(mao_cpu)
resp = ganhador(carta_jog, carta_cpu)
if resp == -1:
    ganho_jog = ganho_jog + 1
elif resp == 1:
    ganho_cpu = ganho_cpu + 1
else:
    ganho_jog = ganho_jog + 1
    ganho_cpu = ganho_cpu + 1

if ganho_jog == 3 and ganho_cpu < 3:
    print("Parabéns, você venceu!")
elif ganho_cpu == 3 and ganho_jog < 3:
    print("A Cpu venceu")
else:
    print("Tudo deu empate!")

