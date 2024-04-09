dec = int(input("Informe número na base decimal: "))
bin = ""

while dec != 0: 
    resto = dec % 2
    dec = dec // 2
    bin = str(resto) + bin

print(f"Binário: {bin}")
