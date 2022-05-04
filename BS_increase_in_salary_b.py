# uma empresa concedeu um bônus de 20% para todosseus funcionários com mais de 5 anos de
# empresa e todos os outrosreceberam uma bonificação de 10%.
years_working = int(input('How long have you been working here?\n'))
current_salary = float(input('How much is your salary?\n'))
if years_working > 10:
    increase = current_salary*0.30
else:
    if years_working >= 5:
        increase = current_salary*0.20
    else:
        increase = current_salary * 0.10
new_salary = float(current_salary+increase)
print('Hello! Congratulation, you earn U$ {:.2f} per month\n'
      'Your new salary will be {:.2f}'.format(increase, new_salary))
