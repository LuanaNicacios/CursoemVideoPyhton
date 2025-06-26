print('GERADOR DE PA')
print('-='*10)
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a Razão da PA: '))
t = p
con = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while con <= total:
        print('{} -> '.format(t), end='')
        t += r
        con += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrandos.'.format(total))