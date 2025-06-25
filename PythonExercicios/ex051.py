print('='*30)
print('DEZ TERMOS DE UMA PA')
print('='*30)
pr = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = pr + (10 - 1) * razao
for c in range(pr, decimo + razao, razao):
    print('{} '.format(c), end='-> ')
print('ACABOU!')