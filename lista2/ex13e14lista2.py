dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

if dia < 1 or dia > 31 or mes < 1 or mes > 12:
    print("Data invalida")
elif dia == 31 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    print("Data inválida")
elif mes == 2 and dia > 28:
    if dia == 29 and ano % 400 == 0:
        print("Data válida")
    elif dia == 29 and ano % 4 == 0 and ano % 100 != 0:
        print("Data válida")
    else:
        print("Data invalida")
else:
    print("Data válida!")