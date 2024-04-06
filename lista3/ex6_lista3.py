nota = int(input("Informe a nota: "))
maior = nota
menor = nota

contador = 1

while contador < 20:
    nota = int(input("Informe a nota: "))
    if nota > maior:
        maior = nota
    if nota < menor:
        menor = nota
    contador = contador + 1

print(f"A maior nota é {maior} e a menor é {menor}")