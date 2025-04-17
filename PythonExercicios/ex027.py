n = str(input('Digite seu nome completo: ')).upper().strip()
name = n.split()
print('Prazem em conhecer {}'.format(n))
print('Seu primeiro nome é: {}'.format(name[0]))
print('Seu último nome é: {}'.format(name[len(name)-1]))



