velo = int(input('Qual velocidade você está? '))
mult = (velo - 80) * 7
if velo > 80:
    print('Você estava acima da velocidade permitida e recebeu uma multa de {} reais'.format(mult))
else:
    print('Sua velocidade estava dentro dos limites')
