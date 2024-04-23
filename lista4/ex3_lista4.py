frase = input("Digite a frase: ")
letra = input("Letra: ").lower()
resp = ""
letraM = letra.upper()

for c in frase:
    if c == letra or c == letraM:
        resp = resp + "*"
    else:
        resp = resp + c

print(resp)
