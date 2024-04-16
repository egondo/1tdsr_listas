#algoritmo módulo 10, recebe um número e devolve
#o seu dígito de controle

num = int(input("Digite o número: "))
mult = 2
soma = 0

while num != 0:
    dig = num % 10
    num = num // 10
    prod = dig * mult
    if prod < 10:
        soma = soma + prod
    else:
        soma = soma + prod % 10 + prod // 10

    if mult == 1:
        mult = 2
    else:
        mult = 1

resto = soma % 10
if resto == 0:
    print("DC é 0")
else:
    print(f"DC é {10 - resto}")            