try:
    a = float(input("Digite a: "))
    b = float(input("Digite b: "))
    resultado = a / b
except ZeroDivisionError:
    print("Impossível dividir por zero!")
else:
    print(f"Resultado {resultado}")
