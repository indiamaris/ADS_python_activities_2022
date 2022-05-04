# Questao 1 de 4
# Academico: Indiamaris-RU:3160566
# Calculo simples de valor subtraido a porcentagem ate 99%:
# y-x% == y - 0.x * y
# Exemplo:  200 - 13% == 200 - 0.13*200
print('Bem vindo a loja Indiamaris-RU:3160566')
# recebe do usuario o identificador pessoal.
identificador = int(input('Entre com seu identificador pessoal, por favor:\n'))
# recebe do usuario o valor do produto.
valor_do_produto3160566 = float(input('Entre com o valor do produto, por favor:\n'))
# recebe do usuario a quantidade de produto.
quantidade_do_produto = int(input('Entre com o valor da quantidade, por favor:\n'))
# calculo simples para encontrar o valor bruto da compra.
total_sem_desconto = valor_do_produto3160566 * quantidade_do_produto
# condicao para desconto de 15%
if quantidade_do_produto >= 1000:
    desconto = '15%'
    total_com_desconto = total_sem_desconto - 0.15*total_sem_desconto
# condicao para desconto de 10%
elif quantidade_do_produto >= 100:
    desconto = '10%'
    total_com_desconto = total_sem_desconto - 0.10 * total_sem_desconto
# condicao para desconto de 5%
elif quantidade_do_produto >= 10:
    desconto = '5%'
    total_com_desconto = total_sem_desconto - 0.05 * total_sem_desconto
# condicao geral sem desconto
else:
    desconto = 'nada'
    total_com_desconto = total_sem_desconto
#  impressao do total (sem desconto)
print('O valor sem desconto foi: R$ {} ' .format(total_sem_desconto))
#  a impressao do total com desconto
print('Oi, {}, O valor com desconto foi: R$ {} '
      'Voce obteve {} de desconto '.format(identificador, total_com_desconto, desconto))
