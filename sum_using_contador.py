cont = 1
soma = 0
while cont < 6:
    x = int(input('Insert a {}th number here: \n'.format(cont)))
    soma += x
    cont += 1
print('Sum is {}' .format(soma))
