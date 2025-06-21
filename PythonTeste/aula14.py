'''for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('Fim')'''

'''n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM')'''

# com while pode criar situações de laços indetermidados.
'''resposta = 'S'
while resposta == 'S':
    n = int(input('Digite um valor: '))
    resposta = str(input('Quer continuar? [S/N] ')).upper()
print('FIM')'''

'''for c in range(1, 11):
    print(c)
print('FIM')'''

'''c = 1
while c < 11:
    print(c)
    c += 1
print('-FIM-')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um Valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))
