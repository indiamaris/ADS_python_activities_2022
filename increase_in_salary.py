# uma empresa concedeu um bônus de 20% para todosseus funcionários com mais de 5 anos de
# empresa e todos os outrosreceberam uma bonificação de 10%.
years_working = int(input('How long have you been working here?\n'))
current_salary = float(input('How much is your salary?\n'))
try:
    if years_working < 5:
        increase = current_salary*0.10
        new_salary = current_salary+increase
    elif (years_working >= 5) & (years_working < 30):
        increase = current_salary*0.20
        new_salary = current_salary+increase
    else:
        increase = current_salary*0.30
        new_salary = current_salary+increase

    print('Hello! Congratulation, you earn U$ {:.2f} per month\n'
          'Your new salary will be {:.2f}'.format(increase, new_salary))
except:
    print('Insert a valid number, please')
