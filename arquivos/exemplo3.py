arq = open('cadastro.txt', mode='r')

for lin in arq.readlines():
    print(lin.split('\t'))

arq.close()
