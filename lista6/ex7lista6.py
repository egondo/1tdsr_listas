def duplas(nome, tupla, pos):
    for i in range(pos, len(tupla)):
        print(nome, tupla[i])


nomes = ("Ana", "Bia", "Celi", "Dani", "Elsa", "Fabi")
i = 0
while i < len(nomes):
    duplas(nomes[i], nomes, i+1)
    i = i + 1
