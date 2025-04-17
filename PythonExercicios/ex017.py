from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

''' --- Forma matematica sem importação --- '''

'''co = float(input('Qual o comprimento do Cateto Oposto: '))
ca = float(input('Qual o comprimento do Cateto Adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''