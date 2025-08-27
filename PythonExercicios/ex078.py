list = []
max = 0
min = 0
for c in range(0, 5):
    list.append(int(input(f'Digite um valor: ')))
    if c == 0:
        max = min = list[c]
    else:
        if list[c] > max:
            max = list[c]
        if list[c] < min:
            min = list[c]
print(f'Valores digitados: {list}')
print(f'Maior valor: {max}')
print(f'Menor valor: {min}')

'''GUANABARA CODE'''
listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            men = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitalizado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end='')