# Um aluno, para passar de ano, precisa estaraprovado em todas as matérias que ele está cursando.
# Assuma que a média para aprovação é a partir de 7, e que o aluno cursa 3 matérias,
# somente.Escreva um algoritmo que leia a nota final do aluno em cada matéria, e
# informe na tela se ele passou de ano ou não.

notaA = float(input('Digite sua primeira nota.'))
notaB = float(input('Digite sua segunda nota.'))
notaC = float(input('Digite sua terceira nota.'))
media = (notaA + notaB + notaC) / 3
if media >= 7:
    status = 'aprovado'
else:
    status = 'reprovado'
print('Sua media foi {} e voce esta {}.'.format(media, status))
