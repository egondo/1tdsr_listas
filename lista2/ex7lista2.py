import math

numero = float(input("Informe um número: "))

if numero < 0:
    print(f"Impossível extrair raiz quadrada de {numero}")
    print("Impossível extrair raiz quadrada de ", numero)
else:
    raiz = math.sqrt(numero)
    print(f"A raiz quadrade de {numero} é {raiz:.4f}")
    print("A raiz quadrada de ", numero, " é ", raiz)
