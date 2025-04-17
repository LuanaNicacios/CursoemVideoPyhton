#Exercício 005 -- antecessor e sucessor#

n = int(input('Dígite um número: '))
an = n-1
su = n+1
print('O Antecessor de {} é: {} \nE o Sucessor de {} é: {} \n'.format(n, an, n, su))

# Correção do exercício: utilizando apenas uma variavel, outras formas de fazer o mesmo codigo#
print('-- OUTRA FORMA DE FAZER O MESMO CÓDIGO --')
print('O Antecessor de {} é: {} \nE o Sucessor de {} é: {} \n'.format(n, (n-1), n, (n+1)))