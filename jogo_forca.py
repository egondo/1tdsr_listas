palavra = "Manga"
segredo = ""
erros = 0
i = 0
while i < len(palavra):
    if palavra[i] == ' ':
        segredo = segredo + "   "
    else:
        segredo = segredo + "_ "
    i = i + 1

letras_chutadas = ""
while erros < 6 and "_" in segredo:
    print(f"{segredo}\nerros: {erros}")
    letra = input("Letra: ").lower()

    if not letra in palavra.lower():
        erros = erros + 1

    letras_chutadas = letras_chutadas + letra

    segredo = ""
    for c in palavra:
        if c == ' ':
            segredo = segredo + "   "
        elif c.lower() in letras_chutadas:
            segredo = segredo + c + " "
        else:
            segredo = segredo + "_ "

if erros >= 6:
    print(f"Você foi enforcado, a palavra: {palavra}")
else:
    print(f"Você acertou, a palavra: {palavra}")