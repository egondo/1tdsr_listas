#O programa sorteia um número aleatório entre 1 e 1000.
#O usuário tem 10 chances para encontrar o número e, para cada valor
#chutado, o programa informa se o número é maior, menor ou igual ao
#valor do chute.

import random

sorteado = random.randint(1, 1000)
#print(sorteado)

chute = int(input("Tente adivinhar o número sorteado: "))
if chute > sorteado:
    print("Tente um número menor!")
elif chute < sorteado:
    print("Tente um número maior!")
else:
    print("Você acertou na 1 tentativa")

chute = int(input("Tente adivinhar o número sorteado: "))
if chute > sorteado:
    print("Tente um número menor!")
elif chute < sorteado:
    print("Tente um número maior!")
else:
    print("Você acertou na 2 tentativa")

chute = int(input("Tente adivinhar o número sorteado: "))
if chute > sorteado:
    print("Tente um número menor!")
elif chute < sorteado:
    print("Tente um número maior!")
else:
    print("Você acertou na 3 tentativa")

chute = int(input("Tente adivinhar o número sorteado: "))
if chute > sorteado:
    print("Tente um número menor!")
elif chute < sorteado:
    print("Tente um número maior!")
else:
    print("Você acertou na 4 tentativa")

chute = int(input("Tente adivinhar o número sorteado: "))
if chute > sorteado:
    print("Tente um número menor!")
elif chute < sorteado:
    print("Tente um número maior!")
else:
    print("Você acertou na 5 tentativa")

chute = int(input("Tente adivinhar o número sorteado: "))
if chute > sorteado:
    print("Tente um número menor!")
elif chute < sorteado:
    print("Tente um número maior!")
else:
    print("Você acertou na 6 tentativa")

chute = int(input("Tente adivinhar o número sorteado: "))
if chute > sorteado:
    print("Tente um número menor!")
elif chute < sorteado:
    print("Tente um número maior!")
else:
    print("Você acertou na 7 tentativa")

chute = int(input("Tente adivinhar o número sorteado: "))
if chute > sorteado:
    print("Tente um número menor!")
elif chute < sorteado:
    print("Tente um número maior!")
else:
    print("Você acertou na 8 tentativa")        

chute = int(input("Tente adivinhar o número sorteado: "))
if chute > sorteado:
    print("Tente um número menor!")
elif chute < sorteado:
    print("Tente um número maior!")
else:
    print("Você acertou na 9 tentativa")    

chute = int(input("Tente adivinhar o número sorteado: "))
if chute > sorteado:
    print("Tente um número menor!")
elif chute < sorteado:
    print("Tente um número maior!")
else:
    print("Você acertou na 10 tentativa")    