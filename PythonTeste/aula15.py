'''cont = 1
while cont <= 10:
    print(cont, '...', end='')
    cont += 1
print('-FIM-')'''

'''n = s = 0
while n != 999:
    n = int(input('Digite um valor: '))
    s += n
print('a soma dos valores é {}'.format(s))'''

n = s = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    s += n
print(f'A soma dos valores é: {s}')

#Atualização do Python das F strings
'''
pep: proposta de melhoria do python

print('A soma dos valores é {}'.format(s)) Simplificando essa maneira de fazer
NOVA MANEIRA:
print(f'A soma vale{s}')

nome = Luana
idade = 24
print(f'A {nome:^} tem {idade:.2f} anos.')
'''
