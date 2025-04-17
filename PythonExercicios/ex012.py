#Exercício 12 -- desconto 5%#

p = float(input('Qual o valor do produto? '))
des = p*(5/100)
val = p-des
print('Você recebeu 5% de desconto e seu protudo sairà por: {:.2f} reais ;)'.format(val))

#Correção do exercício 12 #

print('-- FORMA GUANABARA DE FAZER O MESMO CÓDIGO --')
preço = float(input('Qual é o preço do produto? R$'))
novo = preço - (preço * 5 / 100)
print('o produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))