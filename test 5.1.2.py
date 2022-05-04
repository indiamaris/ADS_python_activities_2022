# Faça um  algoritmo que leia o valor total de uma compra ecalcule o valor do pagamento
# final de acordo com a opção escolhida.
# Se a escolha for por pagamento parcelado, calcule também o valor de cada parcela. Ao
# final,apresente o valor total da compra e o valor das parcelas:
# Pagamento à vista – conceder desconto de 5%;
# Pagamento em 3x – o valor não sofre alterações;
# Pagamento em 5x – acréscimo de 2%;
# Pagamento em 10x – acréscimo 8%.

total_bruto = float(input('total bruto'))
parcelamento = int(input('parcelamento: 0,3 5,10'))
if parcelamento == 0:
    total = total_bruto - (total_bruto * 0.05)
elif parcelamento == 3:
    total = total_bruto
elif parcelamento == 5:
    total = total_bruto + (total_bruto * 0.02)
elif parcelamento == 10:
    total = total_bruto + (total_bruto * 0.08)

parcela = total / parcelamento

print('produto parcelado em {} vezes, total a pagar {}, valor da parcela{}'.format(parcelamento, total, parcela))
