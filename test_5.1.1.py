op = input(' + - / * leave')
x = int(input('x'))
y = int(input('y'))
if op =='+':
    res = x+y
elif op == '-':
    res = x-y
elif op == '*':
    res = x * y
elif op == '/':
    res = x/y
else:
    print('Error')

print(res)