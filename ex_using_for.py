# Escreva um algoritmo que calcule a média dos
# números pares de 1 até 100 (1 e 100 inclusos).Implemente o laço usando
# for
#
qtd = 0
sum = 0
for i in range(1, 101, 1):
    if i % 2 == 0:
        sum += i
        qtd += 1
        media = sum / qtd
print(media)
