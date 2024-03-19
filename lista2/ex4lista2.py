time_casa = input("Nome do time da casa: ")
time_visi = input("Nome do time visitante: ")

gols_casa = int(input(f"Informe gols do {time_casa}: "))
gols_visi = int(input(f"Informe gols do {time_visi}: "))

if gols_casa > gols_visi:
    print(f"{time_casa} venceu!")
elif gols_casa < gols_visi:
    print(f"{time_visi} venceu!")
else:
    print("EMPATE")