ladoA = int(input('a'))
ladoB = int(input('b'))
ladoC = int(input('c'))
if ladoA == 0 or ladoB == 0 or ladoC == 0:
    print('not triangle')
elif ladoA > (ladoB + ladoC) or ladoB > (ladoC + ladoA) or ladoC > (ladoA + ladoB):
    print('not triangle')
elif ladoA == ladoB and ladoB == ladoC:
    print('Equilatero')
elif ladoA != (ladoA != ladoC) or (ladoA != ladoB) or (ladoB != ladoC):
    print('Escaleno')
else:
    print('Isoseles')



