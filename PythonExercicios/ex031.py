dis = float(input('Digite a distancia da sua viagem: '))
pas1 = dis * 0.50
pas2 = dis * 0.45
print('Você vai fazer uma viagem de {} KM'.format(dis))
if dis <= 200:
    print('O preço da sua passagem será de: R${:.2f} R$'.format(pas1))
else:
    print('O preço da sua passagem será de: R${:.2f} R$'.format(pas2))

#CODIGO GUANABARA SIMPLIFICADO#
'''
distancia = float(input('Digite a distancia da sua viagem: '))
print('Você esta preste a começa uma viagem de {:.2f} KM'.format(distancia))
preco = distancia * 0.50 if distancia > 200 else distancia * 0.45
print('E o preço da sua passagem será de: R${:.2f} R$'.format(preco))
'''