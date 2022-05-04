# Exercício 6: Reescreva seu programa de cálculo de pagamento com um
# 1.5 o valor de hora de trabalho por hora extra, crie uma função chamada
# calculoPagamento que aceita dois parâmetros(horas e TaxaHora).
# Insira as Horas: 45
# Insira o valor da Hora de Trabalho: 10
# pagamento: 475.0

def salario(hora, valor):
    pagamento = hora * valor
    print('Pagamento final será {}'.format(pagamento))


salario(10,5)
