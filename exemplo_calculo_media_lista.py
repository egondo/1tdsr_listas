def calcula_media(dados): 
    soma = 0
    for nota in dados:
        soma = soma + nota
    return soma / len(dados)

n = int(input("Qtd de alunos: "))
lista_notas = []

contador = 0
while contador < n:
    nota = float(input("Informe a nota: "))
    lista_notas.append(nota)
    contador = contador + 1

media = calcula_media(lista_notas)
print(media)
#print(lista_notas)
