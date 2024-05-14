import random

def cria():
    deck = []
    for v in range(1, 14):
        deck.append( (v, 'O') )
        deck.append( (v, 'E') )
        deck.append( (v, 'C') )
        deck.append( (v, 'P') )
    return deck

def to_str(card):
    if card[1] == 'O':
        naipe = "♦"
    elif card[1] == 'E':
        naipe = "♠"
    elif card[1] == 'C':
        naipe = "♥"
    else:
        naipe = "♣"

    if card[0] == 1:
        return f"A{naipe}"
    elif card[0] == 11:
        return f"J{naipe}"
    elif card[0] == 12:
        return f"Q{naipe}"
    elif card[0] == 13:
        return f"K{naipe}"
    else:
        return f"{card[0]}{naipe}" 

def embaralha(cartas: list):
    for conta in range(200):
        i = random.randint(0, len(cartas) - 1)
        j = random.randint(0, len(cartas) - 1)
        aux = cartas[i]
        cartas[i] = cartas[j]
        cartas[j] = aux

def compra(cartas: list):
    if len(cartas) > 0:
        return cartas.pop(0)
    else:
        return None

def distribui(cartas: list, qtd: int):
    resp = []
    while qtd > 0:
        resp.append(compra(cartas))
        qtd = qtd - 1
    return resp

if __name__ == "main":
    monte = cria()
    #embaralha(monte)
    #for carta in monte:
    #    print(to_str(carta))

    embaralha(monte)
    carta = compra(monte)
    while carta != None:
        print(to_str(carta))
        carta = compra(monte)

