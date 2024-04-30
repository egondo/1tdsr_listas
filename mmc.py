def mmc(a, b):
    x = a
    while x % b != 0:
        x = x + a
    return x

a = int(input("A: "))
b = int(input("B: "))
res = mmc(a, b)
print(res)