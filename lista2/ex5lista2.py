dias_uteis = int(input("Dias uteis: "))
horas_trab = float(input("Horas trabalhadas: "))
sal_hora = float(input("Salário hora: "))

jornada_padrao = dias_uteis * 8

if jornada_padrao < horas_trab:
    #tenho hora extra para calcular
    hora_extra = horas_trab - jornada_padrao
    valor_extra = hora_extra * sal_hora * 1.5
    salario_total = jornada_padrao * sal_hora + valor_extra
    print("Valor hora-extra", valor_extra)
else:
    salario_total = horas_trab * sal_hora

print("Salario Total:", salario_total)

