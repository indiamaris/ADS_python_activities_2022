# Escreva
# um algoritmo que obtenha do usuário um valor inicial e um valor final. Para
# esteintervalo especificado pelo usuário, calcule e mostre na tela
# a) A quantidade de números inteiros e positivos;
# b) A quantidade de números pares;
# c) A quantidade de números ímpares;
# d) A respectiva média de cada um dos itens anteriores.
# Será necessário criar uma variável distinta
# para cada somatório, para cada quantidade e paracada média solicitada.

a = int(input('initial'))
b = int(input('final'))
positive_quantity = 0
positive_sum = 0
pair_quantity = 0
pair_sum = 0
odd_quantity = 0
odd_sum = 0
contador = a
if a < b:
    while contador <= b:
        if contador > 0:
            positive_quantity += 1
            positive_sum += contador
        if contador % 2 == 0:
            pair_quantity += 1
            pair_sum += contador
        else:
            odd_quantity = odd_quantity + 1
            odd_sum += contador
        contador += 1
    odd_media = odd_sum / odd_quantity
    positive_media = positive_sum / positive_quantity
    pair_media = pair_sum / pair_quantity

    print('Positive total is {}'.format(positive_quantity))
    print('Positive sum is {}'.format(positive_sum))
    print('Positive media is {}'.format(positive_media))
    print('Pair total is {}'.format(pair_quantity))
    print('Pair sum is {}'.format(pair_sum))
    print('Pair media is {}'.format(pair_media))
    print('Odd total is {}'.format(odd_quantity))
    print('Odd sum is {}'.format(odd_sum))
    print('Odd media is {}'.format(odd_media))
else:
    print('The initial value HAS to be bigger than final value!')

