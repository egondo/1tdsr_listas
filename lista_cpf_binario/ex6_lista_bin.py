num = int(input("Numero: "))

resultado = ""

while num != 0:
    resto = num % 16
    num = num // 16
    
    if resto == 10:
        resto = "A"
    elif resto == 11:
        resto = "B"
    elif resto == 12:
        resto = "C"
    elif resto == 13:
        resto = "D"
    elif resto == 14:
        resto = "E"
    elif resto == 15:
        resto = "F"
    resultado = str(resto) + resultado

print(resultado)
