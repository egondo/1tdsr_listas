import math

a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

if a == 0:
    print("Não é equação de 2 grau")
else:
    delta = b * b - 4 * a * c
    if delta < 0:
        print("Não tenho raízes reais!")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"As raízes da equação são: {x1} e {x2}")
        