
'''CONDIÇÃO COMPOSTA'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
'''if m >= 7:
   print('Sua média foi: {:.1f} \n Parabéns você foi APROVADO ;)'.format(m))
else:
    print('Sua média foi: {:.1f} \n Infelizmente você ficou a baixo da média é foi REPROVADO T.T'.format(m))'''

'''CONDIÇÃO SIMPLIFICADA'''
print('SUA MEDIA FOI: {:.1f} \n PARABÉNS'.format(m) if m >=7 else 'SUA MÉDIA FOI {:.1f} \n ESTUDE MAIS!'.format(m))

