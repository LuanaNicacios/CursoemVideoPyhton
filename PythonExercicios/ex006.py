# Exercício número 006, -- dobro, triplo e raiz quadrada.#

n = float(input('Dígite um número: '))
d = n*2
t = n*3
r = n**(1/2)
print('O dobro de é {}: {} \n O triplo de {} é: {} \n A Raiz quadrada de {} é: {:.2f} '.format(n, d, n, t, n, r))

# Correção de Exercício: Outras formas de fazer o codigo#
print('-- OUTRA FORMA DE FAZER O MESMO CÓDIGO --')
print('O dobro de é {}: {} \n O triplo de {} é: {} \n A Raiz quadrada de {} é: {:.2f} '
      .format(n, (n*2), n, (n*3), n, (n**(1/2))))