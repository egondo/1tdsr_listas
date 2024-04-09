n = int(input("Informe n: "))

acumulador = 1
i = 1
while i <= n:
    acumulador = acumulador * i
    i = i + 1

print(f"{n}!={acumulador}")    
