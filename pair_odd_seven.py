numberA = int(input('Please, insert numer to check.'))
if (numberA % 2 == 0) & (numberA % 7 == 0):
    print("Its pair and 7 friendly!")
elif (numberA % 2 == 0) & (numberA % 7 != 0):
    print('Its pair and nothing more.!')
elif (numberA % 2 != 0) & (numberA % 7 == 0):
    print("Its odd and 7 friendly!")
elif (numberA % 2 != 0) & (numberA % 7 != 0):
    print('Its odd and nothing more.')
