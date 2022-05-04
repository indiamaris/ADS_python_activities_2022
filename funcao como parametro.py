def imprime(num, fcond):
    if fcond(num):
        print(num)


def par(x):
    return x % 2 == 0


def impar(x):
    return not par(x)


#  principal

imprime(5, impar)
