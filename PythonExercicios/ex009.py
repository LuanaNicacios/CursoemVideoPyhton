#TExercício 009 -- Tabuada.#
n = int(input('Dígite o número que você deseja saber a tabuada: '))
print('--------------------')
print(f'\n {n} x 1 = {n*1}\n', f'{n} x 2 = {n*2}\n', f'{n} x 3 = {n*3}\n', f'{n} x 4 = {n*4}\n', f'{n} x 5 = {n*5}\n',
      f'{n} x 6 = {n*6} \n', f'{n} x 7 = {n*7} \n', f'{n} x 8 = {n*8} \n', f'{n} x 9 = {n*9} \n', f'{n} x 10 = {n*10} \n')
print('--------------------')

#Correção do Exercício 9 -Sem erros - outras formas de fazer#
print('-- OUTRA FORMA DE FAZER O MESMO CÓDIGO --')
print('_' * 12)
print('{} x {:2} = {}'.format(n, 1, n*1))
print('{} x {:2} = {}'.format(n, 2, n*2))
print('{} x {:2} = {}'.format(n, 3, n*3))
print('{} x {:2} = {}'.format(n, 4, n*4))
print('{} x {:2} = {}'.format(n, 5, n*5))
print('{} x {:2} = {}'.format(n, 6, n*6))
print('{} x {:2} = {}'.format(n, 7, n*7))
print('{} x {:2} = {}'.format(n, 8, n*8))
print('{} x {:2} = {}'.format(n, 9, n*9))
print('{} x {:2} = {}'.format(n, 10, n*10))
print('_' * 12)