#Faça uma função que recebe uma tupla de Strings e retorna a maior String de #todos os valores contidos dentro da tupla.

def maior_string(conjunto: tuple):
    max = ""
    i = 0
    while i < len(conjunto):
        texto = conjunto[i]
        if len(texto) > len(max):
            max = texto
        i = i + 1
    return max


dados = ("Computational Thinking", "Domain Driven Design", "Software Engineering", "Front End", "Building Relational Database")

disciplina = maior_string(dados)
print(disciplina)