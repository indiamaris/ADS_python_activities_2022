initial_hour = int(input('initial'))
final_hour = int(input('final'))
while initial_hour > final_hour or initial_hour < 0 or initial_hour > 23 or final_hour < 0 or final_hour > 23:
    initial_hour = int(input('initial'))
    final_hour = int(input('final'))
for h in range(initial_hour, final_hour + 1, 1):
    for m in range(0, 60, 1):
        for s in range(0, 60, 1):
            print(h, ':', m, ':', s, 'h')
