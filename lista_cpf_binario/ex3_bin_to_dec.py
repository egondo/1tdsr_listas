binario = int(input("Informe número binário: "))
acum = 0
pot_dois = 1

while binario != 0:
    dig = binario % 10
    binario = binario // 10
    acum = acum + dig * pot_dois
    pot_dois = pot_dois * 2

print(f"Resposta {acum}")