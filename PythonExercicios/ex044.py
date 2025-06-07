preco = float(input('Qual o valor a pagar: '))
opcao1 = preco * (1 - 0.10)
opcao2 = preco * (1 - 0.05)
opcao3 = preco * (1 + 0.20)
print('=-'*20)
print('[1] A vista ou Pix: 10% de desconto \n'
      '[2] Á vista no cartão: 5% de desconto \n'
      '[3] Até 2 vezes sem juros \n'
      '[4] 3x ou mais: 20% de juros')
print('=-'*20)
pagamento = int(input('Escolha sua forma de pagamento:'))

if pagamento == 1:
    print('Você ganhou um desconto de 10%, sua compra ficou por: {}R$'.format(opcao1))
elif pagamento == 2:
    print('Você ganhou 5% de desconto, sua compra ficou por: {}R$'.format(opcao2))
elif pagamento == 3:
    print('Sua compra foi de 2 vezes sem juros, o valor será de: {}R$'.format(preco))
else:
    print('Você dividiu de 3x ou mais, e recebou 20% de juros. O valor será de: {}R$'.format(opcao3))