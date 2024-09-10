try:
    a = float(input("Digite a: "))
    b = float(input("Digite b: "))
    resultado = a / b
except (ZeroDivisionError, ValueError) as e:
    if type(e) == ZeroDivisionError:
        print("Impossível dividir por zero!")
    else:
        print("Informe direito o numero. ")
else:
    print(f"Resultado {resultado}")
