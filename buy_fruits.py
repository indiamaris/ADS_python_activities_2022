# Escreva um algoritmo em Python
# em que o usuárioescolhe se ele quer comprar maçãs, laranjas ou bananas. Deverá
# serapresentado na tela um menu com a opção 1 para maçã, 2 para laranja e3
# para banana.
# Após escolhida a fruta, deve-se digitar quantas unidades se quercomprar. O
# algoritmo deve calcular o preço total a pagar do produtoescolhido e mostrá-lo
# na tela. Considere que uma maçã custa R$ 2,30,uma laranja R$ 3,60 e uma banana 1,85

orange = float(3.6)
apple = float(2.3)
banana = float(1.85)
print('Which one fruit do you wish?'),
print('\nFor orange digit 1.'),
print('\nfor apple digit 2.'),
print('\nfor banana digit 3 \n'),

fruits_selected = int(input('choose here\n'))
quantity = int(input('how much?'))

if fruits_selected == 1:
    total = orange * quantity

if fruits_selected == 2:
    total = apple*quantity

if fruits_selected == 3:
    total = banana * quantity

print('Total to pay  is U$ {:.2f}.'.format(total))
