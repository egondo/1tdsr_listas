num = int(input("Numero: "))

resultado = ""

resto = num % 16
num = num // 16
resultado = str(resto) + resultado

resto = num % 16
num = num // 16
resultado = str(resto) + resultado 

resto = num % 16
num = num // 16
resultado = str(resto) + resultado 

print(resultado)
