def valida(question, min, max):
    x = int(input(question))
    while ((x < min) or (x > max)):
        x = int(input(question))
    return x
x = valida('digite', 0, 2)
print('you digited {}. Ending'.format(x))