valor = float(input("Informe o valor total: "))

forma_pgto = int(input("Informe a forma de pgto (1-4): "))

if forma_pgto == 1:
    valor = valor - valor * 0.1  #valor = valor * 0.9
    print(f"Valor a ser pago: {valor}")
elif forma_pgto == 2:
    valor = valor - valor * 0.05 # valor = valor * 0.95
    print(f"Valor a ser pago: {valor}")
elif forma_pgto == 3:
    parcela = valor / 2
    print(f"Em 2x {parcela}")
elif forma_pgto == 4:
    valor = valor + valor * 0.07 #valor = valor * 1.07
    parcela = valor / 4
    print(f"Sua compra saiu {valor} em 4x {parcela}")
else:
    print("Forma de pagamento inválida!")