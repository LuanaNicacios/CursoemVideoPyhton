# TESTE DE CORES #

print('\033[7;32;44mOlá, Mundo!\033[m')

# Cores #
a = int(input('Digite um valor: '))
b = int(input('Digite outro valor:'))
print('Os valores digitados foram: \33[1;31m {} \33[m e \33[1;33m {} \33[m !!!'.format(a, b))

# Cores #

nome = input('Digite seu nome: ')
print('Olá, Mundo! Prazer em te conhecer: {} {} {}!!!'.format('\33[1;31m', nome, '\33[1;33m'))

#Outra maneira de fazer as cores#
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',}
print('Olá, Mundo! Prazer em te conhecer: {} {} {}!!!'.format(cores['amarelo'], nome, cores['limpa']))
