frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A apareçe {} vezes na frase'.format((frase.count('A'))))
print('A primeiro letra A apareceu na posiçaõ {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))
