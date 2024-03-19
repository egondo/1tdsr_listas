num_a = float(input("A: "))
op = input("Op: ")
num_b = float(input("B: "))

if op == '+':
    resultado = num_a + num_b
elif op == '-':
    resultado = num_a - num_b
elif op == '*':
    resultado = num_a * num_b
elif op == '/':
    if num_b != 0:
        resultado = num_a / num_b
    else:
        print("Impossível dividir por 0")
        quit()  #System.exit(0);

print("O resultado é ", resultado)
