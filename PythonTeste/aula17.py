num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
num.sort(reverse=True)
num.insert(2, 2)
if 4 in num:
    num.remove(2)
else:
    print('Não achei o número 4')
num.pop(3)
print(num)
print(f'Essa lista tem {len(num)} elementos')

valores = []
for v in valores:
    print(f'{v}...', end='')

valores = list()
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!', end='')
print('Cheguei ao final da lista.')

a = [1, 3, 4, 7]
b = a
b[2] = 8
print(f'A lista A: {a}')
print(f'A lista B: {b}')

a = [1, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'A lista A: {a}')
print(f'A lista B: {b}')

