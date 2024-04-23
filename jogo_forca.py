palavra = "Jabuticaba"
segredo = ""
erros = 0
i = 0
while i < len(palavra):
    if palavra[i] == ' ':
        segredo = segredo + "   "
    else:
        segredo = segredo + "_ "
    i = i + 1

print(f"{segredo}\nerros: {erros}")
letra = input("Letra: ").lower()

segredo = ""
for c in palavra:
    if c == ' ':
        segredo = segredo + "   "
    elif c.lower() == letra:
        segredo = segredo + c + " "
    else:
        segredo = segredo + "_ "

print(f"{segredo}\nerros: {erros}")




