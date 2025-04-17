import math
num = int(input('Dígite um número: '))
raiz = math.sqrt(num)
print('A raiz de um {} é igual a {:.2f}: '.format(num, raiz))

#Importação direta#
#from math import sqrt, floor
#raiz = sqrt(num)
#print('A raiz de {} é igual a {:.2}'.format(num, floor(raiz)))

#A biblioteca random importa números aleatorios para mostra ao usuario.
print('-'*12)
print('Exercício Números Aleatorios')
import random
n = random.randint(1, 100)
print('O seu número aleatorio é: {}'.format(n))
