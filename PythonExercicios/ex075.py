num = (int(input('Digite um Número: ')),
    int(input('Digite outro Número: ')),
    int(input('Digite mais um Número: ')),
    int(input('Digite o último Número: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1} posição')
else:
    print('O valor 3 não foi digitado em nenhum posição')
print('Os valores pares digitados foram', end='' )
for n in num:
    if n % 2 == 0:
        print(n, end=' ')