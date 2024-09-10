digitou_certo = False

while not digitou_certo:
    try:
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        salario = float(input("Salario: "))
        digitou_certo = True
    except:
        print("Erro no informe, digite novamente!")
print(f"{nome} {idade} {salario}")
