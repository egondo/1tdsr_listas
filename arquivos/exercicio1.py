import random

def gera_data():
    mes = random.randint(1, 12)
    if mes == 2:
        dia = random.randint(1, 28)
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        dia = random.randint(1, 30)
    else:
        dia = random.randint(1, 31)
    return f"{dia}/{mes}/2023"

lojas = ["Centro", "Lapa", "Paulista"]
produtos = [
    {"prod": "celular", "marca": "LG", "valor": 1860},
    {"prod": "celular", "marca": "Samsung", "valor": 2390},
    {"prod": "smart TV", "marca": "Panasonic", "valor": 2800},
    {"prod": "smart TV", "marca": "Samsung", "valor": 3250},
    {"prod": "lavadora", "marca": "LG", "valor": 4720},
    {"prod": "lavadora", "marca": "Brastemp", "valor": 3120},
    {"prod": "geladeira", "marca": "Brastemp", "valor": 5826},
    {"prod": "geladeira", "marca": "Panasonic", "valor": 4590}        
]

datas = {}
with open('faturamento.txt', mode="w") as arq:
    i = 0
    while i < 5000:
        d = gera_data()
        while d in datas:
            d = gera_data()
        datas[d] = True

        for p in produtos:
            for loja in lojas:
                lin = f"{p['prod']};{p['marca']};{loja};{d};{random.   randint(10, 100)};{p['valor']}"
                arq.write(lin + "\n")
        i = i + 24
        