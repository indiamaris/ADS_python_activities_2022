soma = 0
cont = 1
while cont <= 5:
    x = int(input('insira o {} numero.'.format(cont)))
    soma = soma + x
    cont = cont + 1
    media = soma / 5

print('somatorio {} e media {}'.format(soma, media))
