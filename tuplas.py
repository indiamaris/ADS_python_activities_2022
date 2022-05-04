def soma(*num):
    soma = 0
    print("tuplas:{}.".format(num))
    for i in num:
        soma += i
    return soma






# Programa principal
print(soma(1, 2, 3, 4, 5, 6))
