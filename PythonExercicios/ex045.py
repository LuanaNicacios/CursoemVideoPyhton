from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)
print('OPÇÕES:')
print('[0] PEDRA \n'
      '[1] PAPEL \n'
      '[2] TESOURA')
jogador = int(input('Escolha sua opção: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-='*15)
print('O Computador escolheu {}'.format(itens[pc]))
print('O Jogador escolheu {}'.format(itens[jogador]))
print('-='*15)
if pc == 0: #PEDRA
    if jogador == 0: #PEDRA
        print('EMPATE')
    elif jogador == 1: #PAPEL
        print('JOGADOR VENCE')
    elif jogador == 2: #TESOURA
        print('COMPUTADOR VENCE')
    else:
        print('Jogada INVALIDA!')
elif pc == 1: #PAPEL
    if jogador == 0: #PEDRA
        print('COMPUTADOR VENCE')
    elif jogador == 1: #PAPEL
        print('EMPATE')
    elif jogador == 2: #TESOURA
        print('JOGADOR VENCE')
    else:
        print('Jogada INVALIDA!')
elif pc == 2: #TESOURA
    if jogador == 0: #PEDRA
        print('JOGADOR VENCE')
    elif jogador == 1: #PAPEL
        print('COMPUTADOR VENCE')
    elif jogador == 2: #TESOURA
        print('EMPATE')
    else:
        print('Jogada INVALIDA!')