#Exercício 10 -- Conversor de dolar#
r =float(input('Dígite quantos reias você tem: '))
con = r/6.12
print('O valor de {} reis em dolar é: {:.3f} '.format(r, con))

#Correção do exercício 10 -sem erros-#
print('-- OUTRA FORMA DE FAZER O MESMO CÓDIGO --')
r =float(input('Quanto dinheiro você tem na carteira? R$'))
con = r/6.12
print('com R${:.2f} você pode comprar US${:.2f}'.format(r, con))