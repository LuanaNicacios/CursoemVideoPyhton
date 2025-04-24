from random import randint
n1 = int(input('Já pensei em um numero... \n Agora digite o seu: '))
n2 = randint(0,5)
if n1 == n2:
    print('O PALPITE FOI: {} \n PARABÉNS VOCÊ ACERTOU O PALPITE ;)'.format(n2))
else:
    print('O PALPITE FOI: {} \n VOCÊ ERROU O PALPITE T.T'.format(n2))
