# Escreva um algoritmo que calcule e exiba a
# tabuada de um número escolhido e digitado pelousuário. A tabuada deve ser
# calculada até um determinado número
# n
# , também fornecido pelousuário.
# Implemente o laço usando
# for
# .
numberA = int(input('numer'))
for i in range(0, 11):
    total = i * numberA
    print('numer {} times {} is {}'.format(numberA, i, total))
