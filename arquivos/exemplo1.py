import random

def gera_telefone():
    ddd = random.randint(11, 89)
    tel = random.randint(10000000, 99999999)
    return f"({ddd}) 9{tel}"

def gera_nascimento():
    mes = random.randint(1, 12)
    if mes == 2:
        dia = random.randint(1, 28)
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        dia = random.randint(1, 30)
    else:
        dia = random.randint(1, 31)
    ano = random.randint(1935, 2005)
    return f"{dia}/{mes}/{ano}"


nomes = ["Ana", "Antonio", "Amanda", "Beto", "Barbara", "Carlos", 
         "Carina", "Daniel", "Davi", "Dora", "Eduardo", "Eva", 
         "Edna"]
sobrenomes = ["Almeida", "Prado", "Duarte", "Silva", "Lopes", "Gomes",
              "Poderoso", "Figueiredo", "Mello", "Vargas"]


with open("cadastro.txt", mode="w") as arq:
    i = 0
    while i < 5000:
        x = random.randint(0, len(nomes) - 1)
        y = random.randint(0, len(sobrenomes) - 1)

        full_name = nomes[x] + " " + sobrenomes[y]
        arq.write(full_name)
        arq.write('\t')
        arq.write(gera_nascimento())
        arq.write("\t")
        arq.write(gera_telefone())
        arq.write("\n")
        i = i + 1
        