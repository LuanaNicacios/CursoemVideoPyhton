from random import randint
pc = randint(1, 10)
print('Acabei de pensar em um número entre 1 e 10.')
print('Você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais... Tente novamente.')
        elif jogador > pc:
            print('Menos... Tente novamente.')
print('ACERTOU com {} tentativas. PARABÉNS!'.format(palpites))
