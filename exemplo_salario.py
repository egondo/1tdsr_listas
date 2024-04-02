salario = float(input("Informe o salário: "))

while salario < 0:
    print("Salário inválido!")
    salario = float(input("Digite novamente o salário: "))

minimo = 1412.00

qtd_salario_minimo = salario / minimo

print(f"{salario} corresponde a {qtd_salario_minimo:.2f} salários mínimos")