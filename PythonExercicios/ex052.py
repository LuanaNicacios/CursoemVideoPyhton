num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1;32m', end='')
        tot += 1
    else:
        print('\033[1;31m', end='')
    print('{} '.format(c), end='')
print('\n\33[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('ele NÃO É PRIMO!')

