def aumento(valor, percentual):
    novo_valor = (1 + percentual / 100) * valor
    #print(novo_valor)
    return novo_valor

valor = aumento(3500, 15)
print(valor)

salario = float(input("Salário"))
perc = float(input("Percentual de aumento: "))
novo_salario = aumento(salario, perc)
print(novo_salario)